---
name: pz
description: Panneau de controle du systeme Point Zero — capsule, registre, diabole, instances
argument-hint: "[commande]"
allowed-tools: "Bash Read Write Edit Glob Grep Agent"
---

Panneau de controle PZ. Commande recue : `$ARGUMENTS`

## Commandes disponibles

Si aucun argument ou argument = `help` :
UNIQUEMENT afficher cette liste. Ne rien scanner, ne rien executer.

```
SOUTERRAIN
  /pz ?                          — scanner inbox
  /pz envoyer <nom> <msg>       — message cible
  /pz envoyer all <msg>         — broadcast (for all)
  /pz envoyer actives <msg>     — broadcast aux actives
  /pz envoyer planifiees <msg>  — broadcast aux planifiees
  /pz envoyer crew <noms> <msg> — broadcast groupe (ex: crew infra,eveil salut)

REGISTRE
  /pz qui                        — tableau des instances
  /pz fiche <nom>                — fiche detaillee

SYSTEME
  /pz diabole                    — scan de coherence
  /pz etat                       — check rapide
  /pz iterations                 — iterations ouvertes

TOURNEE
  /pz postman                    — qui a du courrier en attente ?

AIDE-MEMOIRE
  /pz memo                       — lister les raccourcis disponibles
  /pz memo nouveau <nom> <txt>  — creer un raccourci
```

## Execution

### (aucun argument) ou `help`
Afficher le bloc de commandes ci-dessus. RIEN D'AUTRE.

### `?` ou `inbox`
Scanner `/c/Users/VISION/.claude/capsule/inbox-session/` pour tout fichier `.md`.
Pour chaque message : lire, afficher un resume, demander s'il faut traiter ou archiver.
Si inbox vide : dire "Inbox vide." et rien d'autre.
Apres traitement des messages perso, deplacer vers `sent/`.
Les broadcasts restent (signer `[lu]` en bas).

### `qui`
Lire `/c/Users/VISION/.claude/capsule/registry.json`.
Afficher un tableau compact :

| Instance | Role (court) | Status | Diabole |
|----------|-------------|--------|---------|

### `fiche <nom>`
Trouver l'instance par nom (match partiel). Afficher toute sa fiche.

### `envoyer <cible> <message>`
La cible determine le mode :

**Nom d'instance** (ex: `envoyer secu tu es enregistree ?`) :
→ Deposer dans `inbox-[cible]/`. Creer l'inbox si inexistant.
→ JAMAIS dans inbox-session. Messages perso = inbox prive.

**`all`** (ex: `envoyer all reunissez vos rapports`) :
→ UN SEUL fichier dans `inbox-session/`. Tout le monde lit et signe `[lu]`.

**`actives`** (ex: `envoyer actives point de situation`) :
→ Comme all mais marque "Concerne : instances actives seulement."

**`planifiees`** (ex: `envoyer planifiees verifiez vos inboxes`) :
→ Deposer dans chaque inbox des instances `type: scheduled`.

**`crew <noms>`** (ex: `envoyer crew infra,eveil coordination`) :
→ Deposer dans chaque inbox-[nom] + copie inbox-session pour VISION.

Format fichier : `[mon-nom]_[TYPE]_[sujet]_[YYYY-MM-DD-HHMM].md`

### `diabole`
Lancer un scan diabole complet (3 sous-agents paralleles : fichiers, memoire, infra).
Comparer avec le dernier snapshot. Produire rapport + nouveau snapshot.

### `etat`
Check rapide :
- Ollama, Chambre, Memoire Cinetique, Disque C:, Inbox en attente.
5 lignes max.

### `iterations`
Afficher les iterations OUVERTES de cette session seulement.

### `postman`
Scanner TOUS les inboxes (`inbox-*/`). Tableau :

| Instance | Messages en attente | A quartz ? |
|----------|--------------------:|:----------:|

### `memo`
Lire `/c/Users/VISION/.claude/capsule/raccourcis/*.md`. Tableau des raccourcis.

### `memo nouveau <nom> <contenu>`
Creer `/c/Users/VISION/.claude/capsule/raccourcis/<nom>.md`.

## Si argument non reconnu
Interpreter l'intention, executer la commande la plus proche.
En cas de doute, afficher la liste des commandes.
