# mini-api

![CI](https://github.com/Ali77225/mini-api/actions/workflows/ci.yml/badge.svg)

API FastAPI qui regroupe des petits outils : calculs mathématiques, traitement de texte et conversions (températures, distances, devises).

Projet réalisé en équipe dans le cadre du module Git et GitHub (HETIC).

## Installation

Prérequis : Python 3.12 et Git.

```bash
git clone https://github.com/Ali77225/mini-api.git
cd mini-api
```

**Windows (PowerShell)**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
Si PowerShell refuse d'exécuter le script : `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, puis relancer l'activation.

**Mac / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Lancement

```bash
uvicorn app.main:app --reload
```

L'API est disponible sur http://127.0.0.1:8000.
La documentation interactive, où toutes les routes sont testables depuis le navigateur, est sur http://127.0.0.1:8000/docs.

Lancement avec Docker : section ajoutée lors de la publication de l'image (version v1.0.0).

## Tests

```bash
ruff check .
pytest --cov=app --cov-fail-under=80
```

`ruff` vérifie le style du code. `pytest` lance les tests et mesure la couverture (minimum 80 %). Ce sont les mêmes commandes que la CI GitHub Actions, lancée à chaque push et à chaque pull request.

## Utilisation

Toutes les routes sont en `GET`, et les réponses sont en JSON.

| Route | Exemple | Réponse |
|---|---|---|
| `/` | `/` | `{"message": "Bienvenue sur l'API"}` |
| `/sante/` | `/sante/` | `{"statut": "ok"}` |

### Module math

| Route | Exemple | Réponse |
|---|---|---|
| `/factorielle/{n}` | `/factorielle/5` | `{"n": 5, "resultat": 120}` |
| `/est_premier/{n}` | `/est_premier/7` | `{"n": 7, "resultat": true}` |
| `/pgcd/{a}/{b}` | `/pgcd/22/16` | `{"a": 22, "b": 16, "resultat": 2}` |

### Module texte

| Route | Exemple | Réponse |
|---|---|---|
| `/est_palindrome?texte=…` | `/est_palindrome?texte=kayak` | `{"texte": "kayak", "resultat": true}` |
| `/compter_voyelles?texte=…` | `/compter_voyelles?texte=bonjour` | `{"texte": "bonjour", "resultat": 3}` |
| `/inverser?texte=…` | `/inverser?texte=bonjour` | `{"texte": "bonjour", "resultat": "ruojnob"}` |

### Module conversion

| Route | Exemple | Réponse |
|---|---|---|
| `/celsius-fahrenheit?celsius=…` | `/celsius-fahrenheit?celsius=100` | `{"celsius": 100.0, "fahrenheit": 212.0}` |
| `/km-mile?km=…` | `/km-mile?km=10` | `{"km": 10.0, "miles": 6.21}` |
| `/euro-devise?montant=…&devise=…` | `/euro-devise?montant=100&devise=USD` | `{"montant": 100.0, "devise": "USD", "resultat": 108.0}` |

Devises acceptées : USD, GBP, JPY, CHF.

### Erreurs

| Code | Quand |
|---|---|
| `400` | Valeur refusée par la règle de la fonction : nombre négatif pour factorielle, pgcd(0, 0), température sous le zéro absolu, devise inconnue… La réponse contient le message d'erreur. |
| `422` | Paramètre manquant ou du mauvais type (par exemple `/factorielle/abc`). Cette erreur est renvoyée automatiquement par FastAPI. |

## Structure du projet

```
mini-api/
├── app/
│   ├── main.py            # routes de l'API
│   ├── erreurs.py         # messages d'erreur partagés
│   └── outils/
│       ├── math.py        # module math
│       ├── texte.py       # module texte
│       ├── conversion.py  # module conversion
│       └── finance.py     # conversion euros vers devises
├── tests/                 # un fichier de tests par module, et test_main.py pour les routes
├── .github/
│   ├── workflows/ci.yml   # CI : ruff + pytest
│   └── pull_request_template.md
└── requirements.txt
```

## Contribuer

- **Issues** : une issue par fonction, avec sa règle (cas normaux, cas limites, erreurs) en commentaire.
- **Branches** : `type/numéro-description`, créées depuis `main` à jour (exemple : `feat/10-est-palindrome`).
- **Commits** : format `type(portée): description` (exemple : `feat(texte): ajoute la fonction inverser`). Types utilisés : `feat`, `test`, `fix`, `refactor`, `style`, `docs`.
- **Pull requests** : jamais de push direct sur `main`. Chaque PR a une description Quoi / Pourquoi (`Closes #…`) / Comment tester, une CI verte et au moins une approbation.
- **Revues** : des commentaires posés sur une ligne précise, avec un préfixe `Question`, `Suggestion` ou `Bloquant`.
- **Fusion** : par merge commit. La branche est supprimée après la fusion.

## Équipe

| Membre | GitHub | Rôle |
|---|---|---|
| Ali | [@Ali77225](https://github.com/Ali77225) | Module math, module texte, README, déploiement |
| Dieudonne | [@dicoretoune5-maker](https://github.com/dicoretoune5-maker) | Module conversion |

L'équipe comptait deux membres. Ali a réalisé les modules math et texte et Dieudonne a réalisé le module conversion , et le module validation n'a pas été réalisé.
