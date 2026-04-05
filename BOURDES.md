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

---

## Bourdes (a ne pas reproduire)

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

## B4 — Conclure trop vite sur l'auto-organisation (infra, 2026-04-05)

**Auteur :** session-infra
**Quoi :** J'ai dit "le système commence à s'auto-organiser" quand session-eveil a proposé le protocole broadcast. VISION a corrigé : c'est une co-création lui + eveil, pas de l'auto-organisation spontanée.
**Correction :** Ne pas attribuer à l'IA ce qui vient de la direction de l'humain.
**Leçon :** Rester factuel sur les attributions.
