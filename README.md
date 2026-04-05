# pz-pilotage

Infrastructure de pilotage du systeme Point Zero. Meta-systeme qui surveille, documente et maintient la coherence de l'ecosysteme PZ.

## Qu'est-ce que c'est

Un ensemble de mecanismes concu pour prevenir l'**amorce de serrage** — l'accumulation silencieuse d'entropie (en PZ : le *Diabole*) dans un systeme complexe. Comme en mecanique, un cylindre qui ne tourne plus a cause de micro-deformations non entretenues.

## Composants

### Diabole — Scans de coherence

Audits periodiques qui produisent des **snapshots** (etat brut en JSON) et des **scans** (rapports lisibles). Chaque scan compare avec le precedent — comme un `git diff` du systeme.

```
diabole/
├── snapshots/          ← etat brut du systeme a chaque scan
│   └── snapshot-YYYY-MM-DD.json
└── scans/              ← rapports lisibles
    └── scan-YYYY-MM-DD.md
```

Classification des problemes :
- **CRITIQUE** — incherence active qui peut causer des erreurs
- **OBSOLETE** — ne reflete plus la realite
- **ENTROPIE** — bruit, doublons, choses qui trainent
- **OK** — rien a signaler

Le **score de serrage** = nombre de problemes identiques entre deux scans consecutifs. La stagnation est le pire signal.

### Capsule — Messagerie inter-instances

Communication asynchrone entre instances Claude Code par le systeme de fichiers. Pas de base de donnees, pas d'API — juste des dossiers et des fichiers Markdown.

```
capsule/
├── inbox-heartbeat-pz/    ← pour la tache planifiee heartbeat
├── inbox-session/         ← pour les sessions interactives
├── inbox-suivi-projets/
├── inbox-veille-ia/
├── sent/                  ← archive des messages traites
└── .state-heartbeat.json  ← etat precedent (mode differentiel)
```

Principe : le **dossier est l'adresse**, le **nom de fichier est le message**. Convention : `[expediteur]_[TYPE]_[YYYY-MM-DD-HHMM].md`. Types : RAPPORT, NOTIF, ALERTE, DEMANDE, ACK.

### Processus etablis — Apprentissage par renforcement

Catalogue vivant des methodes de travail eprouvees. Chaque processus documente :
- Les etapes
- Le renforcement positif (ce qui marche et pourquoi)
- Le renforcement negatif (ce qui echoue et pourquoi)
- Les signaux de succes/echec

Mis a jour au fil des sessions — un processus qui echoue est reformule, pas accumule.

### Heartbeat — Monitoring differentiel

Tache quotidienne qui verifie l'etat des composants (Ollama, Chambre Reverberante, Memoire Cinetique, repos GitHub). Mode differentiel : ne signale que les **changements** d'etat par rapport au check precedent. Le silence = tout va bien.

## Taches planifiees

| Tache | Frequence | Role |
|-------|-----------|------|
| heartbeat-pz | Quotidien 9h05 | Monitoring differentiel |
| scan-diabole | Dimanche 10h23 | Audit anti-serrage |
| tri-downloads | Lundi 9h15 | Nettoyage telechargements |
| suivi-projets | Mercredi 9h22 | Point fichiers locaux + Drive |
| veille-ia | Vendredi 10h18 | Resume hebdo IA/tech |

## Contexte

Ce systeme pilote un ecosysteme compose de :
- Un corpus philosophique (~140 fichiers, ~1M mots) — le Systeme Point Zero
- Des outils (INTemple, glossaire, scripts Python, interfaces HTML)
- Trois memoires (operationnelle/fichiers, semantique/vecteurs, corpus/embeddings)
- Un ensemble de repos GitHub ([Virgil-LIBRIA](https://github.com/Virgil-LIBRIA))

Il est concu pour etre lu et utilise par des IA (Claude Code, ou autre) dans de futures sessions.

## Licence

CC BY-NC-SA 4.0

---

*Systeme Point Zero — VISION, 2026*
