# Declenchement Diabole — 3 cas

> Architecture de declenchement des scans de coherence.
> Statut : Cas 1 et 2 actifs. Cas 3 en design.

---

## Cas 1 — Ponctuel (proactif ou sur demande)

**Declencheur :** VISION dit "scan diabole" OU l'instance detecte que c'est pertinent
et le propose/entreprend d'elle-meme (ex: apres un travail prolifique, apres
beaucoup de modifications de fichiers, quand l'entropie s'accumule visiblement).
**Execution :** Dans la session courante, 3 sous-agents paralleles.
**Statut :** Actif depuis 2026-04-05.

## Cas 2 — Cyclique (periodique)

**Declencheur :** Tache planifiee `scan-diabole`, dimanche 10h23.
**Execution :** Instance autonome, depose rapport dans capsule/inbox-session/.
**Statut :** Actif depuis 2026-04-05. Frequence fixe (hebdomadaire).

**Evolution future :** Frequence intelligente — adapter le rythme au volume
d'activite de la semaine. Plus de sessions productives = scan plus frequent.
Le cron natif ne fait que de la frequence stricte. La partie "intelligente"
(adapter la frequence au contexte) serait du custom.
(Projet — le reglage de la chronicite est en attente d'inspiration.)

## Cas 3 — Par detection de poids data (automatique)

**Principe :** "Pour l'IA le temps c'est de l'espace." Quand le contexte
devient massif, c'est le signal qu'il y a eu beaucoup de travail et donc
potentiellement de l'entropie accumulee.

**Signaux possibles (complementaires, pas exclusifs) :**
- **PreCompact hook** (natif) — se declenche quand le contexte atteint ~80% de la fenetre.
  Utile mais INSUFFISANT seul : plus le contexte augmente (1M+), plus le seuil
  est loin = signal de moins en moins frequent. A combiner avec d'autres signaux.
  Bonus : c'est aussi le bon moment pour archiver intelligemment la conversation
  (epurer les doublons evidents, intra-liens vers la premiere occurrence).
- **Nombre d'iterations** — si > N echanges, la session est longue.
  Les iterations = clockwork (marqueur temporel de l'IA). INDEPENDANT du contexte.
- **Volume de fichiers modifies** — si > N fichiers touches dans une session,
  la surface de modification est grande = risque d'incoherence.
- **Nombre de sous-agents lances** — proxy du volume d'architecture fondee.

**Archive vivante (vision future) :**
A l'approche de la compaction, creer une archive intelligente de la session :
- Pas un dump brut (cf. le transcript VES de 545 Ko = inutilisable)
- Epurer UNIQUEMENT l'evident (copier-coller repetes → intra-lien a la 1ere occurrence)
- Garder le reste tel quel — l'archive vivante est consultable, pas resumee
(Projet futur — ne pas implementer maintenant.)

**Implementation possible (hook PreCompact) :**
```json
{
  "hooks": {
    "PreCompact": [{
      "type": "command",
      "command": "echo 'Session longue detectee. Envisager un mini-scan diabole avant compaction.'"
    }]
  }
}
```

Le hook injecte un rappel dans le contexte au moment de la compaction.
Claude peut alors proposer un scan ou le faire silencieusement.

**Alternative capsule :** Au lieu d'un hook, le scan pourrait etre delegue
a une instance separee (via capsule/inbox-scan-diabole/) pour ne pas
encombrer le contexte de la session productive.

**Statut :** Design pose. Implementation en attente de l'inspiration de VISION.

---

## Note sur l'UI des taches planifiees

Les taches planifiees creees via `create_scheduled_task` sont specifiques
a la section "Code" de Claude. Elles n'apparaissent pas dans Chat/Cowork
et inversement. C'est une isolation par section, pas un bug.

Une tache doit avoir effectue au moins un run pour apparaitre dans l'onglet
"Programme" de l'interface.

---

*Derniere mise a jour : 2026-04-05*
