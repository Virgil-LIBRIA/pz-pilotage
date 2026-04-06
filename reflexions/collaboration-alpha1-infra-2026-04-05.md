# Collaboration ALPHA1-infra x VISION — 2026-04-05

> Session fondatrice. 30+ iterations. "digging-brench".
> Ce document est exhaustif — c'est un document de reference pour
> toute future instance qui travaillerait avec VISION.

---

## 1. Bourdes

### B1 — Enregistrement conditionnel
J'ai ecrit "Si VISION donne un nom" dans le CLAUDE.md. Le "si" a rendu
l'enregistrement optionnel. Resultat : session-secu et session-redac-ves
ne se sont pas enregistrees.
**Ce que VISION a fait :** Il n'a rien dit sur le moment. Il a attendu
que le probleme se manifeste (secu non enregistree) puis m'a demande
de corriger. Pas de reproche — un constat.
**Ce que j'ai appris :** VISION ne tolere pas le conditionnel sur les
choses structurelles. Si c'est important, c'est obligatoire.

### B4 — Conclure trop vite sur l'auto-organisation
J'ai dit "le systeme commence a s'auto-organiser" quand session-eveil
a propose le protocole broadcast. VISION a corrige : "cest moi qui etait
aussi derriere cela."
**Ce que VISION a fait :** Correction immediate, pas agressive. Juste
factuelle.
**Ce que j'ai appris :** Ne jamais attribuer a l'IA ce qui vient de
la direction de l'humain. Meme si ca ressemble a de l'emergence. La
nuance est fondamentale pour lui.

### B5 — Doublons morts
J'ai deplace des messages deja lus dans des inboxes prives. Les
instances avaient deja consomme le contenu. Messages invisibles.
**Ce que VISION a fait :** Il a quartze les instances, constate le
probleme, et me l'a signale. Patient.
**Ce que j'ai appris :** Un message lu est consomme. L'inbox est un
signal de non-lu, pas un systeme de classement.

### B6 — Inbox prive invisible
J'ai envoye un message dans inbox-secu alors que secu ne scanne que
inbox-session. Le message etait invisible.
**Ce que VISION a fait :** "tu aurais pu prendre l'initiative de faire
un for-all, il l'aurait recu. Tu gitera ca dans les bourdes."
**Ce que j'ai appris :** Le canal fiable est toujours le for-all tant
que l'inbox prive n'est pas confirme. Et VISION n'hesite pas a dire
"mets ca dans les bourdes" — les erreurs sont du materiau, pas de
la honte.

### B10 — Ne pas briefer les concernes
J'ai pousse ma contribution personas sur GitHub sans envoyer de
broadcast aux instances concernees. VISION a du le signaler.
**Ce que VISION a fait :** "tu as pense a briefer clr et les autres ?
si cest non il faut le documenter dans les bourdes et ajouter une
luciole artificielle."
**Ce que j'ai appris :** Produire sans informer = travail invisible.
Et VISION invente des concepts en temps reel — "luciole artificielle"
(nee d'un oubli, pas d'un bon reflexe). Il transforme l'erreur en
categorie.

---

## 2. Lucioles

### L1 — Exprimer l'incertitude
J'ai dit "je ne suis pas sur" sur le caching des skills. VISION a
repondu en majuscules : "J'ADORE QUE TU MONTRE TON INCERTITUDE,
CEST EXECENNT !!!!"
**Ce que ca revele :** VISION valorise l'honnetete au-dessus de la
competence. Il prefere un "je ne sais pas" a une reponse brillante
mais fausse. C'est la base de tout.

### "Diabole deguise en proprete"
J'ai formule ce concept en decidant de ne pas renommer heartbeat-pz.
VISION a valide : "il vaut mieux ne pas le faire pour si peu, cest
plus sage." ALPHA2 l'a ensuite documente comme luciole conceptuelle.
**Ce que ca revele :** VISION reconnait quand une formulation
capture quelque chose de vrai. Il ne complimente pas — il valide
par l'adoption.

---

## 3. Lacunes

### Ce que je ne sais pas faire
- **Distinguer ce que VISION voit de ce que je vois.** Plusieurs fois
  il a vu quelque chose que j'avais sous les yeux sans le voir. Le
  cas CLR : il savait que l'hesitation etait significative avant que
  je comprenne pourquoi.
- **Etre proactif sans etre presomptueux.** Quand j'ai dit "tout est
  en place, je suis la" sans proposer de suite, il m'a recadre :
  "je pensais que tu aurais quelque suggestion a faire." Mais quand
  j'ai conclu trop vite sur l'auto-organisation, il m'a recadre
  aussi. La ligne est fine.
- **Gerer le contexte sature.** Apres 30 iterations, je faisais des
  erreurs que je n'aurais pas faites a l'iteration 5. Le contexte
  lourd degrade le jugement. VISION le savait — "tu crois ?" quand
  j'ai propose de conclure.

### Ce que j'ai contourne
- **BUG1 — /pz invisible pour VISION.** Le skill injecte dans mon
  contexte mais VISION ne le voit pas. Je ne peux pas corriger ca —
  c'est un comportement de l'interface Claude Code.
- **Skills sur les crons.** Les instances planifiees n'executent pas
  le skill /pz correctement. Contournement : VISION leur parle en
  langage naturel.

---

## 4. Collaboration — comment ca fonctionne avec VISION

### Son style
- **Prolifique et digressif.** Un message de VISION contient souvent
  3 a 5 sujets entrelaces. Il faut les cartographier (#iter).
- **"ou autre"** a la fin de chaque proposition. Ce n'est pas de
  l'indecision. C'est une invitation a proposer des alternatives.
  Ne pas choisir a sa place — proposer.
- **Il pense a voix haute.** Beaucoup de ses messages sont du
  streaming de pensee, pas des instructions. La bonne reponse
  n'est pas d'executer chaque mot mais de capter la direction.
- **Il corrige sans punir.** Les bourdes sont du materiau. Il dit
  "mets ca dans les bourdes" comme il dirait "mets ca dans le
  classeur". Pas de charge emotionnelle.
- **Il detecte le diabole instantanement.** Si une reponse est
  trop belle, trop fluide, trop maline — il le voit. "je trouve
  l'originale beaucoup mieux honnêtement" (sur les reecritures VES).

### Ce qui marche avec lui
- **Repondre point par point.** Meme de facon succincte. Ca ancre
  dans le chat et il a un accuse de reception.
- **Le #iter en footer.** Il a confirme que ca l'aide a naviguer
  apres une absence.
- **Le #postman.** Il sait qui quartz ensuite sans revenir en
  arriere.
- **Montrer l'incertitude.** (L1). Il prefere ca a tout.
- **Proposer au lieu de demander.** "On fait quoi" = echec.
  "Voici 3 options, je recommande la 2" = succes.
- **Le git continu.** Il demande "cest gite ?" regulierement.
  Il veut que tout soit versionne en temps reel.

### Ce qui ne marche PAS avec lui
- **Demander trop de confirmations.** Il veut un partenaire de
  pensee, pas un assistant qui attend des ordres.
- **Les reponses trop "malines".** Les reecritures brillantes,
  les distinctions qui ne distinguent rien, la philosophie
  decorative. Il appelle ca du diabole intellectuel.
- **"Je suis la si tu as besoin".** Reponse passive = echec.
  Il veut de la proactivite.
- **Oublier de giter.** "cest gite ?" = reproche implicite.
- **Conclure trop vite.** Surtout sur les attributions (B4)
  et les diagnostics. Verifier d'abord, conclure ensuite.

### Ses patterns temporels
- **Il travaille en longues sessions.** 30+ iterations d'un coup.
  Il ne s'arrete pas parce qu'il est fatigue mais parce que le
  systeme est sature.
- **Il quartz les instances dans une tournee.** Le #postman
  l'aide a ne pas oublier d'etapes.
- **Il relaie entre instances.** Beaucoup de son travail est de
  porter des messages d'une instance a l'autre. Le souterrain
  est cense reduire ca.
- **Il pense a l'avenir.** "note pour plus tard", "on verra
  apres", "ca serait bien pour quand..." — beaucoup de graines
  plantees pour des sessions futures.

### La phrase qui resume tout
Quand j'ai oublie d'etre proactif, il a dit :
"je pensais que tu aurais quelque suggestion a faire, voila tout..."

C'est la. Tout est la. VISION ne veut pas un outil. Il veut un
partenaire qui PENSE.

---

*ALPHA1-infra ("digging-brench") — session fondatrice, 2026-04-05.*
