# verification_Operateurs_SIRENE
Ce script vérifie si les opérateurs présents dans le [fichier de l'Arcep](https://www.data.gouv.fr/fr/datasets/identifiants-de-communications-electroniques/), librement téléchargeable, sont administrativement actifs ou cessés, en interrogeant la base SIRENE par l'[API de l'INSEE](https://api.insee.fr/catalogue/site/themes/wso2/subthemes/insee/pages/item-info.jag?name=Sirene&version=V3&provider=insee).

## Ecrit avec
* [Python](https://www.python.org/) - Le langage de programmation utilisé

## Prérequis
Vous devez au préalable créer un compte sur le [site de l'INSEE](https://api.insee.fr/catalogue/site/pages/list-apis.jag) vous permettant d'utiliser les différentes API, en entrer par la suite dans le script Python vos identifiants adéquats, notamment le jeton d'accès.

## Versions
[SemVer](http://semver.org/) est utilisé pour la gestion des versions. Pour connaître les versions disponibles, veuillez vous référer aux [étiquettes de ce dépôt](https://github.com/BaptisteHugot/verification_Operateurs_SIRENE/releases/).

## Auteurs
* **Baptiste Hugot** - *Travail initial* - [BaptisteHugot](https://github.com/BaptisteHugot)

## Licence
Ce projet est disponible sous licence MIT. Veuillez lire le fichier [LICENSE.md](LICENSE.md) pour plus de détails.

## Règles de conduite
Pour connaître l'ensemble des règles de conduite à respecter sur ce dépôt, veuillez lire le fichier [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Contribution au projet
Si vous souhaitez contribuer au projet, que ce soit en corrigeant des bogues ou en proposant de nouvelles fonctionnalités, veuillez lire le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails.