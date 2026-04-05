---
name: pz
description: Panneau de controle du systeme Point Zero — capsule, registre, diabole, instances
argument-hint: "[commande]"
allowed-tools: "Bash Read Write Edit Glob Grep Agent"
---

Panneau de controle PZ. Commande recue : `$ARGUMENTS`

## Commandes disponibles

Si aucun argument ou argument = `help` :
Afficher cette liste a VISION :

```
/pz ?            — scanner les souterrains (inbox-session)
/pz qui          — lister les instances (registre)
/pz fiche <nom>  — afficher la fiche d'une instance
/pz envoyer <nom> <message> — deposer un message dans l'inbox d'une instance
/pz diabole      — lancer un scan diabole
/pz etat         — etat rapide du systeme (ollama, chambre, mem0, disque)
/pz iterations   — afficher les iterations ouvertes de cette session
/pz @all <msg>   — broadcast a TOUTES les instances (tous les inboxes)
/pz @actives <msg> — broadcast aux instances actives seulement
/pz @planifiees <msg> — broadcast aux taches planifiees seulement
```

## Execution

### `?` ou `inbox`
Scanner `/c/Users/VISION/.claude/capsule/inbox-session/` pour tout fichier `.md`.
Pour chaque message : lire, afficher un resume a VISION, demander s'il faut traiter ou archiver.
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

### `@all <message>`
Broadcast a TOUTES les instances. Lire le registre, collecter TOUS les inboxes
(instances + sessions), deposer le meme message dans chacun.
Format : `[mon-nom]_BROADCAST_[sujet]_[YYYY-MM-DD-HHMM].md`
Confirmer a VISION : "Broadcast envoye a N inboxes."

### `@actives <message>`
Comme @all mais filtrer sur `status: active` dans le registre.

### `@planifiees <message>`
Comme @all mais uniquement les instances `type: scheduled`.

## Si argument non reconnu
Traiter comme un message libre — interpreter l'intention et executer la commande la plus proche.
En cas de doute, afficher la liste des commandes.
