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
  /pz ?              — scanner inbox (lire les messages recus)
  /pz envoyer <nom> <msg> — message cible a une instance
  /pz @all <msg>     — broadcast a toutes les instances
  /pz @actives <msg> — broadcast aux actives seulement
  /pz @planifiees    — broadcast aux taches planifiees

REGISTRE
  /pz qui            — tableau des instances
  /pz fiche <nom>    — fiche detaillee d'une instance

SYSTEME
  /pz diabole        — scan de coherence
  /pz etat           — check rapide (ollama, chambre, mem0, disque)
  /pz iterations     — iterations ouvertes de cette session

AIDE-MEMOIRE
  /pz @              — lister les raccourcis @ disponibles
  /pz @nouveau <nom> <contenu> — creer un raccourci @ a la volee
```

## Execution

### (aucun argument) ou `help`
Afficher le bloc de commandes ci-dessus. RIEN D'AUTRE. Pas de scan, pas d'etat.

### `?` ou `inbox`
Scanner `/c/Users/VISION/.claude/capsule/inbox-session/` pour tout fichier `.md`.
Pour chaque message : lire, afficher un resume a VISION, demander s'il faut traiter ou archiver.
Si inbox vide : dire "Inbox vide." et rien d'autre.
Apres traitement, deplacer vers `sent/`.

### `qui`
Lire `/c/Users/VISION/.claude/capsule/registry.json`.
Afficher un tableau compact :

| Instance | Role (court) | Status | Diabole |
|----------|-------------|--------|---------|

Inclure les instances planifiees ET les sessions.

### `fiche <nom>`
Lire le registre, trouver l'instance par nom (match partiel accepte).
Afficher toute sa fiche : role, personnalite, knows, can_do, evolution, meta.

### `envoyer <nom> <message>`
Identifier l'inbox de l'instance cible via le registre.
Creer un fichier `[mon-nom]_DEMANDE_[sujet]_[YYYY-MM-DD-HHMM].md` dans l'inbox cible.
Contenu = le message de VISION, formate en capsule (expediteur, destinataire, type).
Confirmer le depot a VISION.

### `@all <message>`
Broadcast = UN SEUL fichier dans `inbox-session/` (pas de copies dans chaque inbox).
Tout le monde lit et signe `[lu]` au meme endroit.
Format : `[mon-nom]_BROADCAST_[sujet]_[YYYY-MM-DD-HHMM].md`
Confirmer a VISION : "Broadcast depose dans inbox-session."

### `@actives <message>`
Comme @all mais ajouter dans le broadcast : "Concerne : instances actives seulement."

### `@planifiees <message>`
Comme @all mais ajouter dans le broadcast : "Concerne : taches planifiees seulement."

### `diabole`
Lancer un scan diabole complet (3 sous-agents paralleles : fichiers, memoire, infra).
Comparer avec le dernier snapshot. Produire rapport + nouveau snapshot.

### `etat`
Check rapide sans scan complet :
- Ollama : `curl -s http://localhost:11434/api/tags | head -c 100`
- Chambre : `curl -s http://localhost:5002/health`
- Memoire Cinetique : appeler `memory_list` via MCP
- Disque : espace libre sur C:
- Inbox : nombre de messages en attente
Afficher en 5 lignes max.

### `iterations`
Lire le fichier d'iterations de la session en cours (si existe dans le contexte).
Afficher les iterations OUVERTES seulement.

### `@` (liste aide-memoire)
Lire `/c/Users/VISION/.claude/capsule/raccourcis/` pour tout fichier `.md`.
Afficher un tableau :

| Raccourci | Description | Fichier |
|-----------|-------------|---------|

Ce sont des raccourcis que VISION peut utiliser avec @ dans ses prompts
pour injecter du contexte sans devoir se souvenir des chemins.

### `@nouveau <nom> <contenu>`
Creer un fichier `/c/Users/VISION/.claude/capsule/raccourcis/<nom>.md` avec le contenu.
Si le contenu est un chemin de fichier, mettre un pointeur.
Si c'est du texte libre, le stocker directement.
Confirmer la creation.

## Si argument non reconnu
Traiter comme un message libre — interpreter l'intention et executer la commande la plus proche.
En cas de doute, afficher la liste des commandes.
