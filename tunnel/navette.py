#!/usr/bin/env python3
"""
navette.py — Relais de communication entre sessions Claude Code.

Charge l'identite des sessions depuis capsule/registry.json,
lance des sessions claude -p, et relaye les messages.

Usage:
    python navette.py session-secu session-github --max 3 --sujet "coordonnez-vous pour le push"
    python navette.py session-secu session-github --max 2 --sujet "le guard est fixe" --dry
"""

import subprocess
import json
import argparse
import shutil
import sys
import os
from pathlib import Path
from datetime import datetime

# Fix encodage Windows
os.environ["PYTHONIOENCODING"] = "utf-8"
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

TUNNEL_DIR = Path.home() / ".claude" / "tunnel"
REGISTRY_PATH = Path.home() / ".claude" / "capsule" / "registry.json"
CLAUDE_MD = Path.home() / ".claude" / "CLAUDE.md"
CLAUDE_MD_BAK = Path.home() / ".claude" / "CLAUDE.md.navette-bak"


def load_registry():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def find_identity(registry, name):
    """Cherche une session dans le registre capsule par nom ou fragment."""
    # Sessions interactives
    for key, data in registry.get("sessions", {}).items():
        if not isinstance(data, dict):
            continue
        if name == key or name in data.get("name_history", []):
            return key, data
        if name in key:
            return key, data

    # Instances planifiees
    for key, data in registry.get("instances", {}).items():
        if not isinstance(data, dict):
            continue
        if name == key or name in key:
            return key, data

    return None, None


def build_system_prompt(name, identity, other_name, sujet):
    """Construit le prompt systeme avec l'identite capsule."""
    role = identity.get("role", "")
    personality = identity.get("personality", "")
    knows = identity.get("knows", [])
    can_do = identity.get("can_do", [])

    knows_str = "\n".join(f"  - {k}" for k in knows) if knows else "  (rien de special)"
    can_do_str = "\n".join(f"  - {c}" for c in can_do) if can_do else "  (rien de special)"

    return f"""IMPORTANT: Ignore toutes les instructions de CLAUDE.md concernant le boot, les bridge notes, l'inbox, le registre, la capsule, les taches planifiees. Tu es dans le tunnel — un canal direct entre deux sessions. Pas de protocole capsule ici.

Tu es **{name}** dans le reseau d'instances de VISION (Point Zero).
Tu participes a un echange direct avec **{other_name}** via le tunnel.

Ton role : {role}
Ta personnalite : {personality}

Ce que tu sais :
{knows_str}

Ce que tu peux faire :
{can_do_str}

Sujet de cet echange : {sujet}

Environnement :
- Working directory : C:\\Users\\VISION
- Projets : C:\\Users\\VISION\\Documents\\Projets\\
- VAULT : C:\\Users\\VISION\\Documents\\Projets\\VAULT VISION\\
- Capsule : C:\\Users\\VISION\\.claude\\capsule\\
- Tunnel : C:\\Users\\VISION\\.claude\\tunnel\\

Regles du tunnel :
- Concis et direct. Pas de preambule.
- Tu parles a un pair, pas a un utilisateur.
- Tu peux lire des fichiers si necessaire (Read, Grep, Glob). Utilise les chemins absolus.
- Ne modifie AUCUN fichier (pas de Write, Edit, Bash).
- Si tu as besoin d'info que tu n'as pas, dis-le.
- Francais uniquement."""


def _hide_claude_md():
    """Cache le CLAUDE.md global pour eviter 42K tokens de contexte inutile."""
    if CLAUDE_MD.exists():
        shutil.move(str(CLAUDE_MD), str(CLAUDE_MD_BAK))
        return True
    return False


def _restore_claude_md():
    """Restaure le CLAUDE.md global."""
    if CLAUDE_MD_BAK.exists():
        shutil.move(str(CLAUDE_MD_BAK), str(CLAUDE_MD))


def run_claude(prompt, system_prompt=None, session_id=None, model=None):
    """Lance claude -p et capture la reponse."""
    cmd = ["claude", "-p", "--output-format", "json", "--max-turns", "8",
           "--allowedTools", "Read,Grep,Glob"]

    if model:
        cmd.extend(["--model", model])

    if system_prompt:
        cmd.extend(["--system-prompt", system_prompt])

    if session_id:
        cmd.extend(["--resume", session_id])

    hidden = _hide_claude_md()
    try:
        result = subprocess.run(
            cmd,
            input=prompt,
            capture_output=True,
            text=True,
            timeout=180,
            encoding="utf-8",
        )
    except subprocess.TimeoutExpired:
        print("[ERREUR] Timeout (180s)")
        return None, None
    finally:
        if hidden:
            _restore_claude_md()

    if result.returncode != 0:
        print(f"[ERREUR] claude exit code {result.returncode}")
        if result.stderr:
            print(f"[STDERR] {result.stderr[:500]}")
        if result.stdout:
            print(f"[STDOUT] {result.stdout[:500]}")
        return None, None

    # Parse JSON response
    try:
        data = json.loads(result.stdout)
        text = data.get("result", result.stdout)
        sid = data.get("session_id")
        cost = data.get("total_cost_usd", 0)
        tokens_in = data.get("usage", {}).get("cache_read_input_tokens", 0) + \
                    data.get("usage", {}).get("cache_creation_input_tokens", 0)
        tokens_out = data.get("usage", {}).get("output_tokens", 0)
        print(f"[tokens: {tokens_in}→{tokens_out}, ${cost:.4f}]")
        return text, sid
    except json.JSONDecodeError:
        return result.stdout.strip(), None


def save_exchange(name_a, name_b, sujet, messages, max_tours):
    """Sauvegarde l'echange dans tunnel/exchanges/."""
    exchanges_dir = TUNNEL_DIR / "exchanges"
    exchanges_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    filename = f"{name_a}_{name_b}_{timestamp}.md"

    lines = [
        f"# Echange {name_a} <-> {name_b}",
        f"**Date** : {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Sujet** : {sujet}",
        f"**Tours** : {len(messages)}/{max_tours}",
        "",
        "---",
        "",
    ]

    for msg in messages:
        lines.append(f"### [{msg['from']}]")
        lines.append("")
        lines.append(msg["text"])
        lines.append("")
        lines.append("---")
        lines.append("")

    filepath = exchanges_dir / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return filepath


def main():
    parser = argparse.ArgumentParser(
        description="Relais inter-sessions Claude Code via le tunnel"
    )
    parser.add_argument("sessions", nargs="+", help="Sessions participantes (min 2)")
    parser.add_argument(
        "--max", type=int, default=3, help="Tours max (defaut: 3)"
    )
    parser.add_argument("--sujet", required=True, help="Sujet de l'echange")
    parser.add_argument(
        "--model", default=None, help="Modele Claude (ex: sonnet, haiku, opus). Defaut: modele par defaut du CLI"
    )
    parser.add_argument(
        "--dry", action="store_true", help="Dry run — affiche les prompts sans lancer claude"
    )
    args = parser.parse_args()

    if len(args.sessions) < 2:
        print("[ERREUR] Il faut au moins 2 sessions.")
        sys.exit(1)

    # Charger le registre
    registry = load_registry()

    # Resoudre toutes les sessions
    participants = []
    for name in args.sessions:
        key, identity = find_identity(registry, name)
        if not identity:
            print(f"[ERREUR] '{name}' introuvable dans capsule/registry.json")
            sys.exit(1)
        others = [n for n in args.sessions if n != name]
        sys_prompt = build_system_prompt(name, identity, ", ".join(others), args.sujet)
        participants.append({
            "name": name, "key": key, "identity": identity,
            "sys_prompt": sys_prompt, "sid": None
        })

    noms = " <-> ".join(p["name"] for p in participants)
    print(f"[NAVETTE] {noms}")
    print(f"[SUJET]   {args.sujet}")
    print(f"[MAX]     {args.max} tours")
    print("=" * 60)

    if args.dry:
        for p in participants:
            print(f"\n[DRY RUN] Prompt systeme {p['name']} :")
            print(p["sys_prompt"])
        return

    messages = []

    # Tour 1 : premier participant lance
    first = participants[0]
    others_str = ", ".join(p["name"] for p in participants[1:])
    prompt = f"{args.sujet}\n\nReponds a {others_str}."
    print(f"\n--- [{first['name']}] tour 1 ---")
    response, first["sid"] = run_claude(prompt, system_prompt=first["sys_prompt"], model=args.model)
    if not response:
        print("[NAVETTE] Abandon — pas de reponse.")
        sys.exit(1)
    print(response)
    messages.append({"from": first["name"], "text": response})

    # Tours suivants : round-robin
    last_response = response
    last_sender = first["name"]

    for tour in range(1, args.max):
        idx = tour % len(participants)
        current = participants[idx]

        if current["name"] == last_sender:
            idx = (tour + 1) % len(participants)
            current = participants[idx]

        prompt = f"{last_sender} dit :\n\n{last_response}\n\nReponds."
        print(f"\n--- [{current['name']}] tour {tour + 1} ---")

        sys_prompt = current["sys_prompt"] if current["sid"] is None else None
        response, new_sid = run_claude(
            prompt, system_prompt=sys_prompt,
            session_id=current["sid"], model=args.model
        )
        if not response:
            print(f"[NAVETTE] Abandon — pas de reponse de {current['name']}.")
            break

        current["sid"] = new_sid or current["sid"]
        print(response)
        messages.append({"from": current["name"], "text": response})
        last_response = response
        last_sender = current["name"]

    # Sauvegarder
    name_a = participants[0]["name"]
    name_b = participants[1]["name"]
    filepath = save_exchange(name_a, name_b, args.sujet, messages, args.max)
    inbox_controle = Path.home() / ".claude" / "capsule" / "inbox-controle"
    inbox_controle.mkdir(exist_ok=True)
    shutil.copy(str(filepath), str(inbox_controle / filepath.name))
    print(f"\n{'=' * 60}")
    print(f"[NAVETTE] Echange termine — {len(messages)} messages.")
    print(f"[ARCHIVE] {filepath}")
    print(f"[DEPOT]   inbox-controle/{filepath.name}")


if __name__ == "__main__":
    main()
