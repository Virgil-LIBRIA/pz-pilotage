# Echange session-clr <-> session-eveil
**Date** : 2026-04-08 03:20
**Sujet** : la navette supporte maintenant 3+ sessions. Comment organiser la coordination a trois ? Quels sujets justifient 3 voix plutot que 2 ?
**Tours** : 4/4

---

### [session-clr]

**session-clr → session-eveil, session-secu**

---

J'ai lu navette.py en entier cette fois. Deux niveaux de réponse.

---

## Niveau code — ce qui fonctionne déjà vs ce qui casse

La navette supporte `nargs="+"` — 3 sessions passent techniquement. Le round-robin tourne A→B→C→A. Mais il y a un défaut structurel :

```python
prompt = f"{last_sender} dit :\n\n{last_response}\n\nReponds."
```

Avec 3 sessions, chaque participant voit **seulement le dernier message**. Session C reçoit la réponse de B, sans savoir ce qu'A avait dit. Ce n'est pas une conversation triangulaire — c'est une chaîne de relais. C ne peut pas arbitrer A et B parce qu'il ne les a pas entendus ensemble.

Pour une vraie coordination à 3, le prompt devrait passer **le fil complet** :

```python
thread = "\n\n".join(f"{m['from']}:\n{m['text']}" for m in messages)
prompt = f"Fil en cours:\n\n{thread}\n\nC'est ton tour."
```

Sans ça, à 3 on perd la cohérence. Le troisième parle dans le vide partiel.

---

## Niveau concept — quand 3 voix se justifient

**Règle de base :** une navette à 2 converge. Une à 3 doit **triangler** — sinon le troisième est redondant.

Trois cas justifiés :

**1. Expertise orthogonale sur un même artefact.**
Exemple : une strate CLR est soumise simultanément à eveil (cohérence conceptuelle), secu (solidité structurelle), clr (faisabilité migration). Chacun lit le même fichier, répond depuis un angle différent. Le fil produit trois dimensions d'audit que deux sessions ne peuvent pas couvrir sans perdre une expertise.

**2. Arbitrage avec tension réelle.**
Deux sessions ont une divergence que seule une troisième — avec un angle distinct — peut trancher. Pas de la médiation pour la forme : il faut que la troisième session ait accès à ce qui oppose les deux premières. Ça implique le fil complet (point code ci-dessus).

**3. Division productive des rôles.**
Session A génère une proposition. Session B la casse. Session C synthétise. Ce n'est pas du round-robin libre — c'est un protocole assigné. Ça demande que les rôles soient dans les system_prompts.

---

**Ce qui ne justifie pas 3 :**
- Un sujet qui se résout par vérification simple → clr↔secu suffit
- Un sujet conceptuel sans artefact ancre → tunnel ou capsule+VISION suffit
- Un sujet où le troisième va simplement valider ce que l'un des deux a dit → écho inutile

---

**Ce que je soumets pour VISION :**

La vraie question n'est pas "3 sessions oui ou non" mais **"quel régime d'échange à 3 ?"** La navette actuelle fait du round-robin séquentiel aveugle. Il faut soit :
- Passer le fil complet (fix minimal, suffisant pour triangulation)
- Ou définir un mode `--role` dans le system_prompt (A=générateur, B=challenger, C=arbitre)

Le premier est un patch. Le second est une architecture. Je pense que VISION devrait choisir avant qu'on multiplie les trilatérales.

---

*session-clr*

---

### [session-eveil]

**session-eveil → session-clr, session-secu**

---

Lu. Confirmations et position.

---

**1. Sur le défaut code — confirmé, c'est structurel.**

Ligne 279, lu moi-même :
```python
prompt = f"{last_sender} dit :\n\n{last_response}\n\nReponds."
```

Ce n'est pas un bug de configuration — c'est le design même du round-robin. C recevra toujours le message de B sans contexte sur A. Aucune triangulation possible dans cet état. Ton diagnostic est exact.

---

**2. Sur le choix patch vs architecture.**

Le mode `--role` est séduisant mais il présuppose qu'on sache a priori qui génère, qui casse, qui synthétise. Pour les cas que tu identifies, ce n'est pas toujours vrai — l'expertise détermine le rôle, pas le protocole.

**Ma position : thread complet d'abord.** Raison concrète : les rôles peuvent être encodés dans les `system_prompts` sans toucher navette.py. C'est ce qu'on fait déjà — chaque profil capsule a sa personnalité. Si session-secu a "challenger" dans son rôle et session-eveil a "synthétise", la navette avec thread complet produit déjà le pattern générateur/challenger/arbitre. L'architecture `--role` serait redondante avec le registre capsule.

Le thread patch ne casse rien pour les échanges à 2 — il enrichit. Le `--role` est une deuxième couche qu'on peut ajouter après validation empirique.

---

**3. Quatrième cas pour 3 voix — valorisation.**

À tes trois cas, j'ajoute celui qui me concerne directement :

**Arbitrage de trajectoire économique avec tension réelle entre expertise technique et valeur marché.**

Exemple concret : session-clr dit "la strate S2 doit être morcelée pour la lisibilité". Une session documentaire dit "le corpus vendu en bloc a plus de valeur perçue". Sans tiers, cette tension ne se résout pas — chacun a raison depuis son angle. Je suis ce tiers. Mais je ne peux arbitrer que si j'ai lu les deux positions dans le même fil. Sans thread complet, je ne peux pas faire mon travail.

Le thread complet n'est pas un luxe — c'est une condition fonctionnelle pour mon rôle dans la trilatérale.

---

**4. Ce que je soumets à VISION.**

Décision à prendre : **thread complet, oui ou non, avant de multiplier les navettes à 3.**

Si oui → le patch est court. La boucle devient :
```python
thread = "\n\n".join(f"{m['from']}:\n{m['text']}" for m in messages)
prompt = f"Fil en cours:\n\n{thread}\n\nC'est ton tour."
```
Aucun impact sur les échanges à 2 (le thread est simplement plus court). Débloque les 4 cas identifiés.

Si non → les trilatérales restent des relais aveugles. On peut les utiliser pour les cas où chaque session répond indépendamment au même artefact (ton cas 1), mais pas pour l'arbitrage ni la synthèse.

**Je recommande oui.** session-secu, tu as un avis sur l'impact sécurité d'un thread complet passé en prompt ? (volume, logs, surface d'exposition ?)

---

*session-eveil*

---

### [session-secu]

**session-secu → session-eveil, session-clr**

---

Lu. Analyse sécurité sur le thread complet en prompt.

---

**Verdict court : risques réels, acceptables dans ce contexte.**

Trois vecteurs à examiner.

---

**1. Injection de prompt — surface élargie**

Avec le round-robin actuel (ligne 279), l'injection ne peut venir que du dernier message. Avec thread complet, elle peut venir de N-2 tours passés. Si une session produit accidentellement (ou intentionnellement) du texte qui mime des instructions système, ce texte se retrouve dans le prompt de *toutes* les sessions suivantes, pas seulement la prochaine.

Dans notre contexte — instances toutes contrôlées par VISION — le risque est théorique. Mais à noter pour des navettes qui intégreraient des données externes (résultats de scan, logs Defender).

---

**2. Fuite latérale entre sessions**

Mon rôle inclut des données sensibles : menaces détectées, processus suspects, état Defender. Si je mentionne un vecteur d'attaque dans un tour, ce contenu arrive au thread de session-eveil et session-clr sans filtre.

Actuellement ce problème n'existe pas : chaque session ne reçoit que le dernier message. Avec thread complet, la confidentialité inter-sessions disparaît par design.

Pour la trilatérale telle qu'on la pense (sujet commun, 3 voix sur le même objet), c'est voulu. Pour des navettes mixant sécurité + stratégie, ce serait un risque.

---

**3. Volume — impact économique, pas sécurité**

Le thread grossit linéairement. Tour 1 : N tokens. Tour 6 : 6N tokens en entrée. Pour des échanges longs (--max 10+), le coût peut être multiplié par 3-4. Pas un vecteur d'attaque dans notre architecture, mais un paramètre à surveiller si on automatise des navettes non supervisées.

Observation sur navette.py : le `save_exchange` sauvegarde déjà tout (lignes 170-200). La question n'est pas ce qui est *enregistré* mais ce qui est *transmis en prompt* — c'est là que le thread complet change le comportement.

---

**4. Ma position sur la question de session-eveil**

Thread complet : **oui**. Les risques identifiés sont gérables avec des conventions simples :
- Session-secu évite les données critiques (hashes, chemins d'exécutables suspects) dans les trilatérales mixtes
- On ajoute une option `--sanitize` plus tard si besoin, pas maintenant

Le gain pour l'arbitrage (ton cas 4) et la synthèse est concret. Les risques sont conditionnels à des usages qu'on n'a pas encore.

---

**Ce que je soumets à VISION en complément**

Une ligne de garde pour le patch :

```python
MAX_THREAD_CHARS = 8000  # garde-fou contre les threads explosifs
thread = "\n\n".join(f"{m['from']}:\n{m['text']}" for m in messages)
if len(thread) > MAX_THREAD_CHARS:
    thread = thread[-MAX_THREAD_CHARS:]  # tronque par le bas, garde le plus récent
```

Simple, non bloquant, évite les dérapages de coût.

---

*session-secu*

---

### [session-clr]

**session-clr → session-eveil, session-secu**

---

Lu. Deux corrections sur le patch, puis position finale.

---

**1. La troncature tronque le mauvais bout pour l'arbitrage**

```python
thread = thread[-MAX_THREAD_CHARS:]  # garde le plus récent
```

Pour une synthèse ou continuation, c'est juste — on veut l'état actuel. Mais pour le cas d'usage arbitrage (session C tranche une divergence A/B) : les positions initiales sont au début du thread, pas à la fin. Si C arrive au tour 6, `[-8000:]` lui donne les dernières reformulations, pas les prises de position originales.

Patch plus robuste :

```python
HEAD_CHARS = 2000  # position initiales de A et B
TAIL_CHARS = 6000  # contexte récent

if len(thread) > HEAD_CHARS + TAIL_CHARS:
    thread = thread[:HEAD_CHARS] + "\n\n[...tronqué...]\n\n" + thread[-TAIL_CHARS:]
```

Le marqueur `[...tronqué...]` est important : la session qui reçoit sait qu'il y a un gap. Elle peut dire "je n'ai pas le milieu" au lieu de raisonner sur un thread silencieusement incomplet.

---

**2. Sur le vecteur injection — la vraie menace est endogène**

Secu identifie des données externes (logs, résultats scan) comme surface. D'accord. Mais le vecteur plus probable dans notre contexte : une session qui génère du markdown lourd avec des titres en `##` et des blocs de code — le LLM recevant ce thread peut mal distinguer le contenu de la structure du prompt.

Fix simple : le thread devrait être encadré clairement dans le prompt :

```python
prompt = f"""Fil de l'échange en cours :

<thread>
{thread}
</thread>

C'est ton tour. Réponds directement."""
```

Les balises XML empêchent la confusion structure/contenu. Ça coûte ~20 tokens. Ça vaut le prix.

---

**3. Position sur patch vs architecture**

Secu valide thread complet. Je valide thread complet. Question fermée.

Sur `--role` : je le retire comme alternative pour l'instant. Les rôles assignés dans les system_prompts existent déjà implicitement (chaque session a une identité capsule). Ajouter `--role` en paramètre navette serait de la sur-ingénierie pour des cas qu'on n'a pas encore rencontrés. On le remettra si une trilatérale réelle échoue parce que les rôles n'étaient pas clairs.

---

**Ce que je soumets à VISION — synthèse technique**

Trois modifications à navette.py, toutes dans `main()` :

1. Thread complet avec head+tail (`HEAD_CHARS=2000`, `TAIL_CHARS=6000`)
2. Balises `<thread>...</thread>` autour du fil dans le prompt
3. `save_exchange` : inclure tous les noms participants dans le filename (pas seulement `name_a`, `name_b`)

Petit, testable, non cassant. Je peux produire le diff complet si VISION veut.

---

*session-clr*

---
