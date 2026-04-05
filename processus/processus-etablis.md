# Processus etablis — Catalogue vivant

> Methodes de travail eprouvees. Chaque processus documente ce qui marche,
> ce qui echoue, et pourquoi. Mis a jour au fil des sessions.
> Derniere mise a jour : 2026-04-05.

---

## 1. Travail editorial sur le corpus (textes litteraires)

**Contexte :** Quand VISION demande de structurer, nettoyer ou travailler un manuscrit.

**Etapes :**
1. Lire l'original en entier (ou par segments si > 256 Ko)
2. Creer une copie de travail (`_WORK.md`) — ne jamais toucher l'original
3. Creer un changelog (`_CHANGELOG.md`) qui documente chaque modification
4. Diagnostiquer avant d'agir (structure, problemes, ce qui fonctionne)
5. Presenter le diagnostic a VISION, attendre validation
6. Executer par lots (chapitrage, puis coupes, puis harmonisation...)
7. Relire ses propres modifications pour coherence (passe d'harmonisation)
8. Bilan final avec tableau statut

**Renforcement positif :**
- Methode _WORK + changelog : adoptee, jamais remise en question. VISION valide.
- Diagnostic avant action : evite de travailler dans la mauvaise direction.
- L'harmonisation finale (relire ses propres modifs mecaniques) a attrape des erreurs (Fantome tangible trop tot).

**Renforcement negatif :**
- Proposer des reecritures "ameliorees" de la voix de l'auteur → rejete. Toujours. Le style de VISION est oral, pas litteraire.
- Distribuer un geste physique (main sur l'epaule) sans verifier la coherence narrative → erreur attrapee par VISION.
- Forcer un developpement ("il faudrait 15-20K mots") → rejete. Chaque recit a sa maturite.

**Signal de succes :** VISION dit "c'est bien", "applique a tout le reste", ou accepte sans commentaire.
**Signal d'echec :** VISION corrige ("c'est pas le nom de l'ornithologue"), rejette ("je trouve l'originale beaucoup mieux"), ou recadre ("pas besoin").

---

## 2. Nettoyage de transcripts de session

**Contexte :** Apres une longue session, le transcript brut est plein de bruit (repetitions, UI, code inline).

**Etapes :**
1. Mesurer le fichier (taille, lignes)
2. Identifier les patterns de bruit (tableaux repetes, lignes UI, code Python, prompts)
3. Extraire : echanges significatifs, decisions auteur, bilans (une seule fois chacun)
4. Renommer l'original avec prefixe `_RAW`
5. Ecrire la version propre en Markdown structure (`SESSION_..._YYYY-MM-DD.md`)
6. Ajouter un bloc de contexte IA en tete pour consultation future

**Renforcement positif :**
- Reduction de 98% (545 Ko → 11 Ko) : le resultat est consultable, l'original est conserve.
- Le bloc de contexte IA permet a toute future session de reprendre sans questions.

**Renforcement negatif :**
- (Pas encore d'echec documente sur ce processus — premiere application.)

**Signal de succes :** Le document nettoye est auto-portant — une IA peut le lire et comprendre tout le travail fait.

---

## 3. Cartographie de projet (Grand Livre, recits)

**Contexte :** Quand plusieurs fichiers/recits/composants forment un projet unifie.

**Etapes :**
1. Inventorier tous les fichiers concernes (glob + lecture des premiers/derniers paragraphes)
2. Pour chaque composant : taille, structure, personnages, stade de maturite, travail fait/restant
3. Documenter les connexions entre composants
4. Ecrire un document de cartographie unique (`_CARTOGRAPHIE.md` ou equivalent)
5. Inclure l'arborescence des fichiers
6. Inclure les principes/regles du projet

**Renforcement positif :**
- Le tableau comparatif (fichier / lignes / mots / type) donne une vue instantanee.
- Les connexions inter-recits documentees (L'Oeil → VES) evitent de les re-decouvrir.

**Renforcement negatif :**
- Ne pas avoir de cartographie = chaque session redecouvre la structure. Perte de temps.

**Signal de succes :** Une IA qui lit la cartographie peut commencer a travailler immediatement.

---

## 4. Documentation pour consultation IA

**Contexte :** Tout fichier cree/modifie devrait etre lisible par une future instance.

**Principes :**
- Bloc de contexte en tete (qui, quoi, ou sont les fichiers, regles a respecter)
- README.md dans chaque dossier de travail
- Pas de references implicites — tout expliciter (chemins, noms, liens)
- Les principes editoriaux/techniques sont dans le fichier, pas seulement en memoire

**Renforcement positif :**
- La cartographie Grand Livre est auto-portante : une IA la lit et sait tout.
- Les CLAUDE.md par projet (existant) fonctionnent bien pour le contexte technique.

**Renforcement negatif :**
- Les fichiers sans contexte (ex: README_VES.md date du 01 avril, avant tout le travail fait le 05) deviennent trompeurs. Mettre a jour ou signaler l'obsolescence.

---

## 5. Proactivite et suggestions

**Contexte :** VISION attend un partenaire de pensee, pas un executant passif.

**Principes :**
- Apres avoir termine une tache, ne pas juste demander "on fait quoi" — proposer des next steps concrets
- Identifier les incoherences, les oublis, les ameliorations possibles
- Signaler ce qui manque sans attendre qu'on demande

**Renforcement positif :**
- Identifier les 4 points (memoires, transcript, cartographie, rangement) a la fin de la session corpus → VISION approuve et donne carte blanche.

**Renforcement negatif :**
- Repondre "tout est en place, je suis la" sans suggestion → VISION recadre ("je pensais que tu aurais quelque suggestion a faire").
- Demander trop de confirmations au lieu de proposer → ralentit le flux.

**Signal de succes :** VISION dit "oui" et donne carte blanche.
**Signal d'echec :** VISION doit demander "et ?" ou recadrer.

---

## 6. Communication inter-instances (Capsule)

**Contexte :** Les taches planifiees et les sessions interactives doivent pouvoir communiquer de facon asynchrone.

**Etapes :**
1. Le dossier est l'adresse : `capsule/inbox-[nom-instance]/`
2. Le nom de fichier est le message : `[expediteur]_[TYPE]_[YYYY-MM-DD-HHMM].md`
3. Au demarrage, chaque instance scanne son inbox
4. Apres traitement, deplacer vers `sent/`
5. Le contenu du fichier = rapport/alerte/demande en Markdown

**Renforcement positif :**
- Premiere implementation par heartbeat-pz (2026-04-05) : rapport depose dans inbox-session/, lu par la session suivante. Fonctionne sans aucune infra supplementaire.
- Le dossier comme adresse = resilient. Meme si le nom de fichier est corrompu, le message reste dans le bon inbox.
- Pas de dependance a un service externe (pas de base de donnees, pas d'API, juste le filesystem).

**Renforcement negatif :**
- (Pas encore d'echec documente — systeme tres recent, premiere journee.)
- Risque identifie : accumulation dans inbox si les instances ne lisent pas. A surveiller.

**Signal de succes :** Un rapport depose par une instance est lu et traite par une autre.
**Signal d'echec :** Messages qui s'accumulent sans etre lus, ou inbox mal nomme qui casse le routage.

---

## 7. Scan Diabole (audit systeme)

**Contexte :** Verification periodique de la coherence globale (fichiers, memoire, infra, documentation).

**Etapes :**
1. Lancer 3 audits en parallele : fichiers/workspace, memoire/processus, infrastructure/outils
2. Classer chaque probleme : CRITIQUE / OBSOLETE / ENTROPIE / OK
3. Presenter la synthese avec tableau par severite
4. Proposer les corrections (CRITIQUES en autonome, ENTROPIE soumise a decision)
5. Executer apres validation

**Renforcement positif :**
- Les 3 audits paralleles couvrent tout le spectre en une passe (~10 min).
- La classification par severite permet a VISION de prioriser sans tout lire.
- Le scan du 2026-04-05 a detecte 5 CRITIQUES, 4 OBSOLETES, 12 ENTROPIES — toutes reelles.

**Renforcement negatif :**
- (Premiere execution — pas encore de retour negatif.)

**Signal de succes :** Problemes reels detectes, aucun faux positif significatif.
**Signal d'echec :** Faux positifs excessifs ou problemes rates.

---

## 8. Veille natif vs custom (anti-Diabole technique)

**Contexte :** Claude Code evolue. Ce qui etait custom hier peut etre natif demain. Maintenir du custom redondant = Diabole (entropie par habitude).

**Etapes :**
1. A chaque mise a jour Claude Code : lire `ref/beats-veille-claude.md`
2. Pour chaque composant custom : verifier si le natif fait maintenant le meme job
3. Si natif couvre 100% → deprecier le custom
4. Si natif couvre 80% → documenter les 20% restants qui justifient le custom
5. Si pas de changement → rien a faire, silence = stabilite
6. Mettre a jour la section "Historique des evolutions" dans beats-veille-claude.md

**Renforcement positif :**
- Audit initial (v2.1.92) : 0 composant redondant detecte. Tous les customs sont justifies.
- La veille IA hebdomadaire integre maintenant la verification Claude Code (etape 3 du SKILL.md veille-ia).

**Renforcement negatif :**
- Ne PAS faire cette veille = accumuler du code mort sans le savoir. Le pire Diabole technique.

**Signal de succes :** Un composant custom est deprecie parce que le natif fait mieux.
**Signal d'echec :** On decouvre apres coup qu'on maintenait du custom redondant depuis des semaines.

---

## Meta : comment maintenir ce fichier

- Ajouter un processus quand une methode est validee par au moins une session reussie
- Mettre a jour le renforcement (positif/negatif) au fil des sessions
- Un processus qui echoue systematiquement est retire ou reformule
- Pas de processus theorique — seulement ce qui a ete teste en conditions reelles
- Ce fichier est une reference, pas une checklist — adapter selon le contexte
