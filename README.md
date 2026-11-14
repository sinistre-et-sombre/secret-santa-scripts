# Secret Santa Sinistre & Sombre Scripts

## Utilisation

Vous pouvez lancer le script avec la commande suivante :

```sh
INSCRIPTIONS_RECFILE=inscriptions.rec.example python scripts_secret_santa_sinistre_sombre
```

Vous obtiendrez alors quelques lignes de texte, utilisable dans [Secret Santa d’Arcanis](https://github.com/arcanis/secretsanta/).

## Configuration

Les scripts Python ici présent sont configurés via des variables d’environnement.

| Nom                    | Valeur par défaut  |
|------------------------|--------------------|
| `INSCRIPTIONS_RECFILE` | `inscriptions.rec` |

## Données

Les données utilisent des [Recfiles](https://www.gnu.org/software/recutils/).

### Fichier `INSCRIPTIONS_RECFILE`

Ce fichier contient les données des inscrit·e·s.
Un exemple est donnée dans [`inscriptions.rec.example`](./inscriptions.rec.example).


