# Steady Fire — page statique

Page d’accueil publique minimale de **Steady Fire 2**.

## Contenu du paquet

- `index.html` — la page complète, avec styles intégrés ;
- `favicon.svg` — icône locale ;
- `.nojekyll` — publication directe sans traitement Jekyll ;
- `robots.txt` — autorisation d’indexation ;
- `INSTALLATION_PAS_A_PAS.md` — procédure GitHub Pages + Namecheap.

Le fichier `CNAME` n’est volontairement **pas** présent dans le paquet initial. La page peut ainsi être contrôlée d’abord sur son adresse GitHub Pages. Après vérification du domaine et validation de la page, GitHub créera ce fichier lorsque `steadyfire.ai` sera déclaré dans **Settings > Pages > Custom domain**.

## Propriétés

- aucune base de données ;
- aucun JavaScript ;
- aucun formulaire ;
- aucune clé ou donnée privée ;
- aucun outil d’analyse ;
- aucune ressource externe chargée par la page ;
- site adaptatif pour ordinateur et téléphone.

## Dépôt conseillé

Créer un dépôt public dédié nommé :

```text
steadyfire.ai
```

Puis placer tous les fichiers de ce dossier à la racine de la branche `main`.

La procédure complète figure dans [`INSTALLATION_PAS_A_PAS.md`](INSTALLATION_PAS_A_PAS.md).
