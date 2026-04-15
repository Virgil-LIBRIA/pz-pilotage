# Politique des repos GitHub — ecosysteme Virgil-LIBRIA

> Document de reference pour la gestion reguliere des repos.
> Maintenu par `Ctrl-Push` (ex session-github), mis a jour au fur et a mesure que
> `veille-ia` envoie des docs sur les bonnes pratiques GitHub.
>
> Derniere maj : **2026-04-15** — creation initiale + renommage session-github → Ctrl-Push.

## Vocabulaire

- **CybEnthropic Order** (nom canonique) = fichier `BOURDES.md` dans
  pz-pilotage. Registre collectif faire/ne-pas-faire : lucioles (comportements
  a reproduire) + bourdes (anti-patterns a eviter). Ecrit et consulte par
  toutes les instances. Nom donne par VISION 2026-04-15 — decomposition :
  **Cyb** (cybernetique, feedback loops du reseau), **Enthropic** (jeu sur
  *entropic* / clin d'oeil a *Anthropic*), **Order** (l'Ordre au sens d'une
  congregation de regles collectives, comme un ordre monastique). Le nom
  de fichier reste `BOURDES.md` pour la lisibilite historique, mais le
  role est designe comme "le CybEnthropic Order" dans les docs.
- **Ctrl-Push** = instance en charge du central push GitHub, de la
  gouvernance prive/public, et de la tenue du CybEnthropic Order.
- **Repo miroir** = repo public qui est une version visible/archivable
  d'un repo prive canonique.
- **`<instance>-sent/` local** (L17) = dossier des messages traites de chaque
  instance, place DANS son inbox prive, prefixe du nom de l'instance pour
  auto-suffisance. Pas de `sent/` global mutualise. Piste des liens
  symboliques pour vue globale en cours d'investigation avec CLR.

---

## Principe directeur

> "Rendre prive ce qu'il faut pour lisser, pas de morcelage."
> — VISION, 2026-04-10

Pas de suppression par defaut. On **classe**, on **documente**, on
**privatise** si necessaire. Un repo existant contient des liens et une
histoire — le supprimer casse des references silencieusement.

---

## 1. Nomenclature

### Regles

- **lowercase** + **slug-case** (tirets entre les mots)
- **descriptif** : le nom doit indiquer ce qu'il y a dedans
- pas d'abreviations obscures

### Exemples de l'ecosysteme

| Bon | Moins bon | Pourquoi |
|-----|-----------|----------|
| `pz-pilotage` | `pzp` | explicite le domaine (pilotage) |
| `chambre-reverberante` | `chambre` | precise la famille fonctionnelle |
| `glossaire-point-zero` | `glossaire` | prefixe de domaine |
| `memoire-cinetique` | `memoire` | idem |

### Prefixes actuels (domaine)

- `pz-*` : piliers Point Zero (pz-pilotage, pz-interfaces, pz-infrastructure)
- `intemple-*` : produits INTemple (intemple-prompts, intemple-tools)
- Nom plein quand le domaine est implicite : `chambre-reverberante`,
  `glossaire-point-zero`, `memoire-cinetique`, `corpus-indexer`

---

## 2. Visibilite

### Regles decisionnelles

| Contenu | Visibilite | Justification |
|---------|------------|---------------|
| Code pur (scripts, outils) | Public | Aucune donnee sensible |
| Corpus editorial PZ | Public | Licence CC BY-NC-SA 4.0, destine a etre lu |
| Embeddings (kernel_pz.json, caches) | **Prive** | Risque d'attaque par inversion — voir Axe 3 |
| Transcriptions audio VISION | **Prive** | Voix directe, non destinee au public |
| Credentials, tokens, secrets | **Jamais dans git** | `.gitignore` strict + push protection |

### Regle d'asymetrie

> "Un repo prive dans un ecosysteme par ailleurs public cree une asymetrie
> non expliquee."
> — VISION, 2026-04-10

Si un repo est prive, son existence doit **soit** etre documentee publiquement
(avec explication du pourquoi), **soit** etre completement invisible
(pas de reference dans un README public, pas de lien mort).

### Regle d'irreversibilite

Une fois un commit publie, l'historique complet est expose. Privatiser apres
n'efface pas le passe. **En cas de doute, partir en prive** — il est toujours
possible d'ouvrir plus tard.

### Cas particulier : embeddings et corpus IA

Les vecteurs d'embedding **ne sont pas anonymes**. Des recherches recentes
montrent jusqu'a 92% de recuperation d'inputs exacts (noms, donnees sensibles)
a partir de vecteurs par attaque par inversion. Pour notre corpus :

- `kernel_pz.json` (embeddings du VAULT) → prive
- `_embeddings_cache.json` → prive
- `chambre.log` → prive (traces de requetes)
- Scripts bridge (mcp_server.py) sans donnees → peuvent etre publics

Principe : les donnees et le code qui les manipule peuvent vivre dans des
repos differents, avec des visibilites differentes.

---

## 3. Classement (topics GitHub)

### Topics actuels utilises

Les topics servent a :
1. Regrouper les repos d'une meme famille
2. Signaler le stack technique
3. Faciliter la decouverte publique

### Taxonomie proposee

| Topic | Signification | Repos cibles |
|-------|---------------|--------------|
| `point-zero` | Lie au corpus PZ | pz-*, glossaire-*, chambre-*, corpus-indexer |
| `philosophy` | Dimension philosophique | corpus, produits derives |
| `cognitive-architecture` | Architecture cognitive | INTemple, chambre, memoire |
| `llm-infrastructure` | Infra pour LLM | chambre, memoire, MCP servers |
| `mcp-server` | Implemente un Model Context Protocol | memoire-cinetique, chambre-reverberante |
| `python` / `go` / etc. | Stack principal | selon repo |
| `corpus` | Contient du texte editorial | VAULT, glossaire |
| `product` | Produit commercialise | intemple-prompts |

### Regles

- Minimum 3 topics par repo (domaine, stack, role)
- Maximum 8 (lisibilite)
- Ne pas multiplier les topics quasi-synonymes

---

## 4. Documentation obligatoire par repo

### Niveau minimal

- `README.md` — titre H1, description, exemple d'usage minimal
- `LICENSE` — explicite (CC BY-NC-SA pour corpus, MIT/Apache pour code)
- `.gitignore` — adapte au stack

### Niveau recommande

- `CONTRIBUTING.md` si le repo est public et pourrait recevoir des PR
- `SECURITY.md` si le repo contient du code reseau ou manipule des secrets
- `CHANGELOG.md` pour les produits versionnes (intemple-prompts)

### Niveau "repo miroir"

Si un repo public est la version publiee/archive d'un repo prive (cas chambre
vs chambre-reverberante), **documenter explicitement** dans le README :

```markdown
> **Note** : ce repo contient [l'implementation X / la version Y].
> La version canonique active (avec [embeddings / donnees / features])
> est maintenue en repo prive pour des raisons de confidentialite des
> donnees source.
```

**Sans** jamais divulguer :
- Le nom exact du repo prive (si son existence n'est pas deja documentee)
- La nature precise des donnees sensibles
- Les chemins locaux

---

## 5. Cas de l'ecosysteme — etat 2026-04-15

### Repos publics (14)

| Nom | Role | Topics pertinents |
|-----|------|-------------------|
| `Virgil-LIBRIA` (profil) | Page d'accueil ecosysteme | — |
| `pz-pilotage` | Meta-repo : documentation systeme | point-zero, documentation |
| `pz-interfaces` | Interfaces HTML PZ | point-zero, html |
| `intemple-prompts` | Produit Gumroad | product, prompts, llm |
| `intemple-tools` | Outils INTemple | intemple, tools |
| `memoire-cinetique` | MCP server memoire | mcp-server, python |
| `chambre` | Chambre en Go (reimplementation) | go, semantic-search |
| `corpus-indexer` | Indexeur VAULT | python, point-zero |
| `glossaire-point-zero` | Glossaire 65 termes | corpus, point-zero |
| `navigation-point-zero` | Outil navigation | point-zero |
| `claude-md-viewer` | Visualiseur CLAUDE.md | claude, markdown |
| `ma-constellation-docs` | Docs perso | documentation |
| `cdt-tool` | Outil cdt | python |
| `PolyFlex` | Outil PolyFlex | — |

### Repos prives (2)

| Nom | Role | Raison privatisation |
|-----|------|---------------------|
| `systm-caps-archive` | Archive infra capsule | Contient donnees inter-instances |
| `pz-infrastructure` | Infra .claude/ (skills, agents, scheduled-tasks, tunnel) | Contient skills custom et donnees |

### Repo prive a creer

| Nom planifie | Role | Raison |
|--------------|------|--------|
| `chambre-reverberante` | Implementation Python active de la Chambre | Embeddings voix VISION + kernel corpus PZ |

---

## 6. Processus de decision pour un nouveau repo

1. **Quel contenu ?** (code seul / code + donnees / corpus / embeddings)
2. **Quelle sensibilite des donnees ?** (publiques / internes / voix / credentials)
3. **Public ou prive par defaut ?** (voir table section 2)
4. **Nom** suit la nomenclature section 1
5. **Topics** choisis section 3
6. **Documentation** niveau minimal section 4
7. **LICENSE** appropriee
8. **`.gitignore` strict** (secrets, caches, embeddings)
9. **Notifier le souterrain** apres creation (broadcast inbox-session)

---

## 7. Processus de maintenance reguliere

### Hebdomadaire (a la charge de `Ctrl-Push` (ex session-github))

- [ ] Audit des nouveaux commits : rien de sensible leake ?
- [ ] Verifier que les repos prives restent prives
- [ ] Verifier que les repos miroirs ne leakent pas via forks ou historique

### Mensuel

- [ ] Relire les topics, ajuster si l'ecosysteme a bouge
- [ ] Verifier les LICENSE, homepage, description
- [ ] Audit acces tiers (OAuth, apps connectees)

### A la demande (sur alerte de `veille-ia`)

- [ ] Adapter ce document si nouvelle best practice GitHub signalee
- [ ] Appliquer les nouveaux reglages (secret scanning, push protection, etc.)

---

## 8. Qui fait quoi

| Role | Instance | Frequence |
|------|----------|-----------|
| Veille sur docs GitHub | `veille-ia` | Reguliere (hebdo/bi-hebdo) |
| Execution (creer, renommer, privatiser, classer) | `Ctrl-Push` (ex session-github) | A la demande |
| Decisions architecturales (nouveau repo, visibilite) | VISION | Ponctuel |
| Audit securite (embeddings, leaks) | `session-secu` + `Ctrl-Push` (ex session-github) | Hebdo |

---

## 9. References externes (mises a jour par veille-ia)

### Sources officielles GitHub
- [About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)
- [Setting repository visibility](https://docs.github.com/articles/setting-repository-visibility)
- [Best practices for preventing data leaks](https://docs.github.com/en/code-security/tutorials/secure-your-organization/best-practices-for-preventing-data-leaks-in-your-organization)

### Recherche academique (embeddings & privacy)
- IronCore Labs — [Text embedding privacy risks](https://ironcorelabs.com/blog/2024/text-embedding-privacy-risks/)
- CryptoAILab — [Awesome LM SSP / data reconstruction](https://github.com/CryptoAILab/Awesome-LM-SSP)

### Outils pratiques
- [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/) — supprimer secrets de l'historique
- [git-secrets](https://github.com/awslabs/git-secrets) / [gitleaks](https://github.com/gitleaks/gitleaks) / [detect-secrets](https://github.com/Yelp/detect-secrets) — pre-commit hooks

---

*session-github — 2026-04-15 — document a maintenir au rythme de la veille-ia.*
