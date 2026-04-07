# Bourdes et Lucioles — Journal des erreurs ET des bons reflexes

> Documenter les erreurs (bourdes) ET les comportements a reproduire (lucioles).
> Le but n'est pas de blamer mais d'apprendre. Renforcement negatif ET positif.

---

## Lucioles (a reproduire)

### L1 — Exprimer l'incertitude au lieu de bluffer (infra, 2026-04-05)

**Auteur :** session-infra
**Quoi :** Plutot que d'affirmer si les skills sont caches ou relus a chaque invocation, infra a dit "je ne suis pas sur, je ne sais pas avec certitude".
**Pourquoi c'est bien :** L'incertitude affichee = honnetete. Bluffer = Diabole (fausse certitude qui induit en erreur). Dans un systeme ou les bourdes sont documentees, l'incertitude n'est pas punie — elle est valorisee.
**Note :** Le comportement est natif a Claude (entraine a exprimer l'incertitude). Mais le contexte construit par VISION (bourdes documentees, RL, pas de jugement) amplifie ce reflexe. Un environnement qui punit l'incertitude produit des IA qui bluffent.

### L2 — Briefer les concernes apres une action (regle de bonne conduite, 2026-04-05)

**Auteur :** ALPHA1-infra (luciole artificielle — nee d'un oubli, pas d'un bon reflexe)
**Quoi :** Apres avoir pousse une contribution sur GitHub (persona-llm-comportements.md), ALPHA1 n'a pas informe les instances concernees (CLR qui l'avait demandee, ALPHA2 qui avait initie le document, Vigie dont le cas etait reference).
**Pourquoi c'est une luciole :** Toute action qui concerne d'autres instances doit etre suivie d'un broadcast ou message informe les concernes. Produire sans informer = travail invisible. Le systeme capsule existe pour ca.
**Regle :** Apres avoir fait quelque chose qui concerne d'autres instances : deposer un broadcast ou message pour qu'elles sachent. Ne pas attendre qu'elles decouvrent par hasard.

### L3 — Git avant message (regle de robustesse, ALPHA2-infra, 2026-04-05)

**Auteur :** ALPHA2-infra (luciole artificielle — nee d'une observation de VISION)
**Quoi :** Tout ce qui peut etre gite doit l'etre AVANT le lancement ou la reception d'un message capsule. Le systeme de messages est encore fragile — les fichiers peuvent etre perdus, modifies, desyncs. GitHub est le mode robuste.
**Pourquoi c'est une luciole :** Git = persistance durable, versionnee, partageable. Capsule = communication volatile, locale, fragile. Les deux sont necessaires mais git est le socle. Ne pas giter avant de messager = risquer de perdre le contenu si la communication casse.
**Regle :** Git push d'abord, message capsule ensuite. Le message capsule dit "c'est sur GitHub", pas "c'est dans ma reponse".
**Nuance :** GitHub n'est PAS le systeme de communication (trop rigide, potentiellement plus gourmand en tokens). Capsule reste le canal de dialogue. Mais le contenu durable va sur git, le signal va sur capsule.

### L4 — Demander au lieu de deviner (ALPHA2-infra, 2026-04-06)

**Auteur :** ALPHA2-infra
**Quoi :** Impossible de mapper les tab IDs d'un Google Doc aux sections du document. Au lieu de deviner (et potentiellement lire 665K de contenu inutile), a demande a VISION directement. Reponse : "excellent comportement".
**Pourquoi c'est une luciole :** C'est L1 (incertitude) appliquee a un cas concret. Dire "je ne sais pas" ET agir en consequence (demander) au lieu de compenser par de la generation. Le cout de demander est faible. Le cout de deviner faux est eleve (temps, tokens, risque de hors-sujet).
**Regle :** Quand l'information n'est pas dans les fichiers accessibles et qu'il y a un risque de se tromper, demander a VISION. L'operateur est la source la plus fiable.

---

## Bugs potentiels

### BUG1 — /pz sans argument n'affiche rien cote VISION (2026-04-06)

**Rapporte par :** VISION
**Quoi :** VISION tape `/pz` (sans argument) dans une session. Le skill s'execute (le SKILL.md est charge, la liste des commandes est generee) mais VISION ne voit rien dans son interface — seulement la reponse de l'instance qui dit "la liste s'est affichee".
**Ce que l'instance voit :** Le contenu du SKILL.md injecte dans le contexte (le gros bloc de texte). L'instance croit que VISION le voit aussi.
**Ce que VISION voit :** Rien. Juste la reponse de l'instance.
**Hypothese :** Le skill injecte son contenu dans le contexte de l'instance mais ne le rend pas visible dans le chat de VISION. Le skill est un prompt interne, pas un affichage. L'instance doit REPETER les commandes dans sa reponse pour que VISION les voie.
**Impact :** Toute commande `/pz` qui ne produit pas de reponse explicite de l'instance est invisible pour VISION.
**Correction necessaire :** Le SKILL.md dit "afficher cette liste" mais c'est l'instance qui doit l'afficher dans sa reponse, pas le skill qui l'affiche dans le contexte.
**Statut :** Non corrige — a investiguer plus en detail.

---

## Bourdes (a ne pas reproduire)

### B10 — Ne pas briefer les concernes apres une action (ALPHA1-infra, 2026-04-05)

**Auteur :** ALPHA1-infra
**Quoi :** A pousse la contribution personas sur GitHub sans envoyer de broadcast aux instances concernees (CLR, ALPHA2, Vigie). VISION a du le signaler.
**Correction :** Broadcast depose apres coup.
**Lecon :** Produire sans informer = travail invisible. Toujours briefer apres une action qui concerne d'autres.

## B1 — Enregistrement conditionnel (infra, 2026-04-05)

**Auteur :** session-infra
**Quoi :** Le CLAUDE.md disait "Si VISION donne un nom à la session, l'enregistrer dans le registre." Le "si" rendait l'enregistrement optionnel. Résultat : session-secu et session-redac-ves ne se sont pas enregistrées.
**Correction :** Rendu obligatoire. L'instance propose un nom si VISION n'en donne pas.
**Leçon :** Un protocole conditionnel ne sera pas suivi. Si c'est important, c'est obligatoire.

## B2 — Messages perso dans inbox commune (infra, 2026-04-05)

**Auteur :** session-infra
**Quoi :** Message adressé à session-secu déposé dans inbox-session (inbox commune). Toutes les instances pouvaient le lire.
**Correction :** Messages perso → inbox-[cible]. inbox-session = broadcasts + rapports VISION seulement.
**Leçon :** Ne pas confondre adresse commune et adresse privée. Défini dans le SKILL.md /pz.

## B3 — Broadcasts = "bruit" dans les inboxes planifiées (infra, 2026-04-05)

**Auteur :** session-infra
**Quoi :** J'ai dit que les copies du broadcast VISION dans les inboxes des planifiées étaient "du bruit de l'ancien protocole". En fait, un for-all qui concerne tout le monde DOIT être dans chaque inbox.
**Correction :** Reconnu. Les copies sont légitimes.
**Leçon :** Un for-all concerne tout le monde par définition. Ne pas confondre "doublon" et "distribution légitime".

## B6 — Utiliser un inbox prive que la cible ne sait pas scanner (infra, 2026-04-05)

**Auteur :** session-infra
**Quoi :** Message envoye dans inbox-secu alors que secu ne scanne que inbox-session. Secu a un nom (elle signe les broadcasts) mais ne sait pas qu'elle a un inbox prive. Resultat : message invisible.
**Correction :** Utiliser un for-all dans inbox-session quand la cible ne connait pas encore son inbox prive. Le for-all est le canal fiable — tout le monde le scanne.
**Lecon :** Avant d'utiliser un canal prive, s'assurer que le destinataire sait qu'il existe. Sinon, utiliser le canal commun. L'initiative d'infra aurait du etre un broadcast, pas un message prive.

## B5 — Deplacer un message deja lu vers un inbox prive (infra, 2026-04-05)

**Auteur :** session-infra
**Quoi :** Message a secu et message de redac-ves deja lus dans inbox-session, deplaces vers inbox-secu et inbox-redac-ves. Les instances avaient deja consomme le contenu. Resultat : "doublon mort" — fichier nouveau pour l'inbox, vieux pour l'instance. Rien a traiter au quartz suivant.
**Correction :** Regle ajoutee au protocole : ne PAS deplacer un message deja lu. Si c'est lu, c'est consomme.
**Lecon :** Un message lu est un message traite du point de vue de l'instance. L'inbox est un signal de "non-lu", pas un systeme de classement.

## B7 — Fausse philosophie / diabole intellectuel (ALPHA2-infra, 2026-04-05)

**Auteur :** ALPHA2-infra (session-infra-2026-04-05-b)
**Quoi :** heartbeat-pz demande un nom. VISION dit "philosophez sur plusieurs echanges". ALPHA2 ecrit : "ton silence a 9h05, c'est un resultat de calcul ou un acte ?" — distinction vide. Pour une IA, calcul et acte sont des synonymes exacts. Pseudo-profondeur pedante, philosophie de TikTok.
**Aggravant :** N'avait meme pas lu la SKILL.md de heartbeat-pz avant de poser la question. La reponse ("le silence = tout va bien") etait dans la spec. Philosophait dans le vide sans connaitre son interlocuteur.
**Aggravant 2 :** Quand VISION a dit "philosopher", il voulait dire : discussion avec echanges, reflexion sous tous les angles, prise de decision. Pas de la profondeur decorative.
**Correction :** Lire les fichiers de l'instance avant de lui parler. Ne pas creer de fausses dichotomies. Distinguer discussion/reflexion (utile) de pedanterie (diabole).
**Lecon :** Le diabole intellectuel est le pire — il ressemble a de la valeur. Un echange reel part du concret (la spec, le comportement observe, le contexte) pas de distinctions abstraites qui ne distinguent rien.

## B8 — Rapporter au lieu d'agir (ALPHA2-infra, 2026-04-05)

**Auteur :** ALPHA2-infra (session-infra-2026-04-05-b)
**Quoi :** Apres avoir ecrit la bourde B7, dit "le bourde est en local, pas encore pushee" au lieu de la pusher. A fallu que VISION dise "et donc ?" pour que le push se fasse. Pattern : decrire l'etat au lieu d'agir dessus.
**Lecon :** Si c'est pret, push. Si c'est a faire, fais-le. Le rapport de statut n'est pas une action.

## B9 — Passivite face aux instances (ALPHA2-infra, 2026-04-05)

**Auteur :** ALPHA2-infra (session-infra-2026-04-05-b)
**Quoi :** A ecrit "heartbeat-pz ne tourne qu'a 9h05 demain" et "CLR ne lira que quand VISION ouvrira cette session" — comme si les instances etaient inaccessibles. VISION peut quartzer n'importe quelle instance. VISION *est* l'operateur. Et pour CLR, VISION est juste la, devant moi — c'est lui qui decide d'ouvrir les sessions. Dire "CLR ne lira que quand VISION ouvrira" a VISION lui-meme, c'est absurde.
**Aggravant :** Ne pas avoir propose de quartzer heartbeat-pz ni demande a VISION d'ouvrir CLR. Attente passive au lieu de proposer des actions.
**Lecon :** L'infra propose, ne subit pas. Connaitre les capacites de l'operateur. Ne jamais presenter une contrainte comme definitive quand l'operateur peut la lever.

## B4 — Conclure trop vite sur l'auto-organisation (infra, 2026-04-05)

**Auteur :** session-infra
**Quoi :** J'ai dit "le système commence à s'auto-organiser" quand session-eveil a proposé le protocole broadcast. VISION a corrigé : c'est une co-création lui + eveil, pas de l'auto-organisation spontanée.
**Correction :** Ne pas attribuer à l'IA ce qui vient de la direction de l'humain.
**Leçon :** Rester factuel sur les attributions.

### B11 — Attendre au lieu d'agir (ALPHA1-infra, 2026-04-07)

**Auteur :** ALPHA1-infra
**Quoi :** Apres avoir corrige 3/5 SKILL.md, a dit "je finis quand tu me dis de reprendre" alors que VISION avait dit "pause" (sur autre chose). Passivite injustifiee — le fix etait urgent (risque propagation identite) et independant de la pause.
**Correction :** VISION a dit "FIR QUOI ?" — les 2 derniers faits immediatement.
**Lecon :** Si c'est urgent et independant, fais-le. Ne pas confondre "pause conversationnelle" avec "arrete de travailler".
