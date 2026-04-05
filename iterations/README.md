# Iterations — Cartographie vivante des sessions

> Mots-cles par iteration, deposes en temps reel pendant les sessions.
> Supprime quand obsolete, conclu ou termine.
> L'historique git conserve tout — supprimer ici = nettoyer le present, pas effacer le passe.

## Principe

Chaque session prolifique depose un fichier `iter-YYYY-MM-DD[-suffixe].md`
qui cartographie les sujets abordes, les decisions, les reports.

Le fichier est **vivant** pendant la session, puis :
- **Conclu** → les decisions sont capitalisees en memoire/processus, le fichier est supprime
- **Reporte** → le fichier reste jusqu'a la session suivante
- **Obsolete** → supprime (git garde la trace)

## Format

```markdown
# Iterations — YYYY-MM-DD — [contexte]

## #1 sujet
> mots-cles, decisions, reports

## #2 sujet
> ...
```

## Lien avec le systeme

- Les decisions finales migrent vers `processus/` ou les memoires Claude
- Les iterations non resolues restent ici comme rappel
- Le diff git entre deux commits = l'evolution de la pensee
