# Capsule — Systeme de communication inter-instances

> Protocole minimaliste, stable, base sur le systeme de fichiers.
> Inspire de Moltbook (reseau social pour agents IA, Matt Schlicht, 2026).

## Principe

Le **dossier est l'adresse**. Chaque instance a son `inbox-[nom]/`.
Le **nom de fichier est le message** (partiel — seul le timestamp change).
Un fichier mal nomme reste dans le dossier → toujours livrable.
Le **registre** (`registry.json`) est l'annuaire — qui existe, quoi faire, comment parler.

## Structure

```
capsule/
├── registry.json              ← annuaire des instances (roles, capacites, canaux)
├── .state-heartbeat.json      ← etat precedent du heartbeat (mode differentiel)
├── inbox-heartbeat-pz/        ← sentinelle quotidienne
├── inbox-scan-diabole/        ← audit anti-serrage hebdo
├── inbox-suivi-projets/       ← point fichiers mercredi
├── inbox-veille-ia/           ← veille IA/tech vendredi
├── inbox-session/             ← sessions interactives de VISION
├── sent/                      ← archive des messages traites
└── README.md                  ← CE FICHIER
```

## Registre d'instances (registry.json)

Chaque instance est declaree avec :

| Champ | Description |
|-------|-------------|
| `type` | scheduled / interactive |
| `role` | Ce que l'instance fait (une phrase) |
| `personality` | Comment elle le fait (ton, style) |
| `knows` | Ce qu'elle sait (donnees, memoires accessibles) |
| `can_do` | Ce qu'elle peut faire (capacites concretes) |
| `reads_inbox` | Son adresse d'entree |
| `writes_to` | A qui elle envoie |
| `schedule` | Quand elle tourne (si planifiee) |

Les sessions interactives s'enregistrent dans `sessions.active` au demarrage
et se retirent a la fin. Les instances planifiees sont permanentes.

## Convention de nommage des messages

```
[expediteur]_[TYPE]_[YYYY-MM-DD-HHMM].md
```

Types : `RAPPORT`, `NOTIF`, `ALERTE`, `DEMANDE`, `ACK`

## Graphe de communication

```
heartbeat-pz ──RAPPORT/ALERTE──→ inbox-session
scan-diabole ──RAPPORT/ALERTE──→ inbox-session
session ──────DEMANDE──────────→ inbox-heartbeat-pz
session ──────DEMANDE──────────→ inbox-veille-ia
session ──────DEMANDE──────────→ inbox-suivi-projets
session ──────DEMANDE──────────→ inbox-scan-diabole
```

Toutes les instances planifiees rapportent a `inbox-session`.
Les sessions interactives peuvent envoyer des DEMANDES a n'importe quelle instance.

## Protocole de demarrage

### Instance planifiee
1. Lire `registry.json` pour connaitre son role et ses canaux
2. Scanner son inbox pour les messages en attente
3. Executer sa tache
4. Emettre dans les inboxes cibles si necessaire
5. Deplacer les messages traites vers `sent/`

### Session interactive
1. Lire `registry.json` pour connaitre les instances disponibles
2. Scanner `inbox-session/` pour les rapports/alertes
3. Mentionner brievement a VISION ce qu'il y a
4. Si VISION nomme la session, l'enregistrer dans `sessions.active`

## Extension future

- `inbox-openclaw/` — synchronise via Drive for Desktop → communication telephone → instances
- Frequence intelligente des scans (adapter au volume d'activite)
- Archive vivante des sessions a la compaction
