# Diabole — Système anti-serrage

> Scans périodiques de cohérence pour prévenir l'amorce de serrage.
> Terme emprunté à la mécanique : un cylindre qui ne tourne plus à cause
> de micro-déformations accumulées sans entretien.
>
> En PZ, le Diabole est la force entropique. Ce système le rend visible.

## Principe

Chaque scan produit un **snapshot** de l'état du système (fichiers, mémoire, infra).
Le scan suivant compare avec le snapshot précédent — comme un `git diff`.
Les **scans** sont les rapports lisibles. Les **snapshots** sont les données brutes.

## Structure

```
diabole/
├── README.md                          ← CE FICHIER
├── snapshots/
│   └── snapshot-YYYY-MM-DD.json       ← état brut du système à date
├── scans/
│   └── scan-YYYY-MM-DD.md            ← rapport lisible (CRITIQUE/OBSOLETE/ENTROPIE/OK)
└── (publie sur GitHub dans le repo système)
```

## Format snapshot (JSON)

```json
{
  "date": "2026-04-05",
  "version": 1,
  "fichiers": {
    "vault_onirique_work": ["ONR_VES_WORK.md", "ONR_ECHOS_WORK.md", ...],
    "a_supprimer_go": 1.4,
    "versions_ves": 16,
    "logs_actions_ok": false
  },
  "memoire": {
    "total_fichiers": 20,
    "index_complet": true,
    "contradictions": 0,
    "processus_documentes": 7
  },
  "infra": {
    "ollama": "up",
    "chambre": "down",
    "memoire_cinetique": "up",
    "docker": "installed_not_running",
    "disque_c_libre_go": 78,
    "repos_github": 11,
    "repos_dirty": 1
  },
  "documentation": {
    "claude_md_a_jour": false,
    "termes_glossaire_declares": [88, 65, 50],
    "termes_glossaire_reels": 90,
    "heartbeat_documente": false
  },
  "compteurs": {
    "critiques": 5,
    "obsoletes": 4,
    "entropie": 12,
    "ok": 15
  }
}
```

## Comparaison (diff)

Le scan compare le snapshot actuel avec le précédent :

| Transition | Signification |
|-----------|--------------|
| critique 5 → 2 | Amélioration : 3 problèmes résolus |
| critique 2 → 5 | Dégradation : 3 nouveaux problèmes |
| entropie 12 → 12 | Stagnation : rien n'a bougé (= amorce de serrage) |
| entropie 12 → 8 | Nettoyage en cours |
| ok 15 → 18 | Système qui se consolide |

**La stagnation est le pire signal.** Quand les compteurs ne bougent pas entre deux scans,
l'entropie s'accumule silencieusement. C'est l'amorce de serrage.

## Fréquence

- **Automatique** : tâche planifiée `scan-diabole` (dimanche 10h)
- **Manuel** : VISION peut demander "scan diabole" à tout moment
- **Post-session** : après une session productive, un mini-scan valide que rien n'a cassé

## Protocole d'exécution

1. Lire le dernier snapshot dans `snapshots/`
2. Scanner les 3 domaines (fichiers, mémoire, infra) en parallèle
3. Produire le nouveau snapshot (JSON)
4. Comparer avec le précédent → générer le diff
5. Écrire le rapport de scan (Markdown) avec :
   - Tableau des transitions (avant → après)
   - Nouveaux problèmes détectés
   - Problèmes résolus depuis le dernier scan
   - Score de serrage (nombre de problèmes stagnants)
6. Si critiques > 0 : émettre ALERTE dans capsule/inbox-session/
7. Pousser snapshot + scan sur GitHub (repo système)

## Lien avec GitHub

Les scans et snapshots sont versionnés sur GitHub — ça crée un historique
consultable par n'importe quelle IA ou par VISION lui-même. Le diff entre
deux commits = l'évolution réelle du système.

Repo : voir `reference_github.md` dans la mémoire Claude.
