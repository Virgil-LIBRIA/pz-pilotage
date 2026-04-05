# Iterations — Cartographie vivante des sessions

> Mots-cles par iteration, deposes en temps reel pendant les sessions.
> Supprime quand obsolete, conclu ou termine.
> L'historique git conserve tout — supprimer ici = nettoyer le present, pas effacer le passe.

## A quoi ca sert

Apres une absence (courte ou longue), VISION peut lire les iterations pour voir :
- **Qui** a parle ou de qui il etait question
- **Quoi** a ete decide, fait, reporte
- **Ou** en sont les chantiers ouverts
- L'**arborescence-timeline** de la session

C'est un outil de navigation temporelle dans les sessions prolifiques.

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
> **CONCLU** / **OUVERT**
```

## Lien avec le systeme

- Les decisions finales migrent vers `processus/` ou les memoires Claude
- Les iterations non resolues restent ici comme rappel
- Le diff git entre deux commits = l'evolution de la pensee
