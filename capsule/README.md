# Capsule — Système de communication inter-instances

> Protocole minimaliste, stable, basé sur le système de fichiers.

## Principe

Le **dossier est l'adresse**. Chaque instance a son `inbox-[nom]/`.
Le **nom de fichier est le message** (partiel — seul le timestamp change).
Un fichier mal nommé reste dans le dossier → toujours livrable.

## Structure

```
capsule/
├── inbox-heartbeat-pz/    ← pour la tâche planifiée heartbeat
├── inbox-suivi-projets/   ← pour la tâche planifiée suivi
├── inbox-veille-ia/       ← pour la tâche planifiée veille-ia
├── inbox-session/         ← pour les sessions interactives de VISION
└── sent/                  ← archive des messages traités
```

## Convention de nommage

```
[expediteur]_[type]_[YYYY-MM-DD-HHMM].md
```

Exemples :
- `heartbeat-pz_RAPPORT_2026-04-05-1200.md`
- `session_NOTIF_UPGRADE_2026-04-05-1430.md`
- `suivi-projets_ALERTE_chambre-down_2026-04-05-0900.md`

Seul le timestamp varie → le glob `*_NOTIF_*.md` capture tout indépendamment du nom exact.

## Types de messages

| Type | Usage |
|------|-------|
| `RAPPORT` | Compte-rendu d'exécution |
| `NOTIF` | Notification légère (pas d'action requise) |
| `ALERTE` | Problème détecté, action possible |
| `DEMANDE` | Requête d'action à l'instance destinataire |
| `ACK` | Accusé de réception |

## Protocole de lecture

À chaque démarrage d'instance :
1. Scanner `capsule/inbox-[nom-instance]/` pour tout `.md`
2. Traiter par ordre chronologique (timestamp dans le nom)
3. Déplacer vers `sent/` après traitement (ou supprimer)
4. Si inbox vide → continuer normalement

## Intégration dans les SKILL.md

Ajouter à chaque tâche planifiée :
```bash
# Lecture inbox capsule
ls /c/Users/VISION/.claude/capsule/inbox-[nom]/*.md 2>/dev/null
```

## Extension future

Le même mécanisme peut router vers des instances distantes (Drive, OpenClaw)
en ajoutant un `inbox-openclaw/` ou en synchronisant via Drive for Desktop.
