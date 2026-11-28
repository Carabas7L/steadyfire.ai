# Steady Fire — site et entrée du corpus H/I

**Statut :** Publication active : site statique, lexique de référence et littérature H/I.  
**Repères documentaires :** Lexique V5 : 27 novembre 2026 ; parcours d’usage : 28 novembre 2026

[Carte des dépôts — commencer ici](https://github.com/Carabas7L/steadyfire.ai/blob/main/docs/CARTE_DES_DEPOTS.md) · [Lexique cœur V5](https://github.com/Carabas7L/steadyfire.ai/blob/main/lexique/Lexique_coeur_v5.0.0.md) · [Concordance des signes](https://github.com/Carabas7L/steadyfire.ai/blob/main/docs/CONCORDANCE.md)

## Objet

Présenter la recherche Steady Fire sur la relation humain–IA, rendre son vocabulaire consultable et publier les œuvres et mandats textuels de Science Friction.

## Contenu disponible

- [Site public](https://steadyfire.ai/) — présentation du laboratoire.
- [Carte des dépôts](docs/CARTE_DES_DEPOTS.md) — rôles, statuts et parcours dans les sept dépôts publics.
- [Note de concordance](docs/CONCORDANCE.md) — sens locaux, évolutions et règles de lecture.
- [Lexique cœur V5](lexique/Lexique_coeur_v5.0.0.md) — référence lexicale ; [lecture sur le site](https://steadyfire.ai/lexique/) et version TXT dans `lexique/`.
- [LAIA-DAIA — cadre de séance pour les usages scolaires](https://github.com/Carabas7L/LAIA-DAIA/blob/main/README.md) — extension d’usage, commandes et annexe scolaire.
- [Science Friction](https://steadyfire.ai/science-friction/) — *La Romance de U/Sola et Igor* et U/RomanceIA V3, mandat textuel à fournir à un modèle de langage.
- `science-friction/downloads/` — PDF et Markdown, édition tout-en-un et empreintes `SHA256SUMS.txt`.

La V4.2 est archivée ; voir la [concordance V4.2 → V5](lexique/CONCORDANCE_V4_V5.md).

## Parcours de lecture

Commencer par la carte. Pour préparer un usage scolaire de l’IA, rejoindre d’abord [LAIA-DAIA et son extension d’usage](https://github.com/Carabas7L/LAIA-DAIA/blob/main/README.md#extension-dusage--préparation-appropriation-et-contrôle-humain-11-novembre-2026), puis consulter le Lexique cœur V5 pour les termes utiles. Pour les autres parcours, choisir un cadre conceptuel ou une publication. Les versions Scala, LAIA-DAIA et Lexique appartiennent à des séries distinctes.

## Limites

Le site publie des documents et des fichiers téléchargeables. Il ne fournit pas de service IA automatisé. Un mandat textuel, une équation ou une description de dispositif ne démontre pas son implémentation ni sa conformité.

## Licence et provenance

Les conditions de réutilisation se lisent dans chaque publication et dépôt concerné. La carte et la concordance ne changent aucune licence. La Romance est présentée sous CC BY-NC-SA 4.0 dans Science Friction.

## Organisation du site

- `index.html` — page d’accueil avec styles intégrés ;
- `lexique/index.html` — lecture du lexique ; sources Markdown et TXT dans le même dossier ;
- `science-friction/index.html` et `read.css` — accueil et styles de lecture ;
- `science-friction/romance/` — chapitres de la Romance ;
- `science-friction/u-romanceia/` — lecture du mandat ;
- `docs/` — carte et concordance consultables sur GitHub ;
- `favicon.svg` — icône locale ;
- `.nojekyll` — publication directe sans traitement Jekyll ;
- `robots.txt` — autorisation d’indexation.

Le fichier `CNAME` est présent à la racine de la branche `main` et contient `steadyfire.ai`, le domaine personnalisé du site publié sur GitHub Pages.

## Propriétés de la page d’accueil

- aucune base de données ;
- aucun JavaScript ;
- aucun formulaire ;
- aucune clé ou donnée privée ;
- aucun outil d’analyse ;
- aucune ressource externe chargée par la page ;
- site adaptatif pour ordinateur et téléphone.
