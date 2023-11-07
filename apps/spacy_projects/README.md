# Project Templates

## Les spaCy Projects

Les [spaCy projects](https://spacy.io/usage/projects) vous permettent de gérer et de partager des workflows spaCy de bout en bout pour différents cas d'utilisation et domaines, et d'orchestrer l'entrainement, le packaging et la distribution de vos pipelines personnalisés. Vous pouvez commencer par cloner un template de projet prédéfini, l'adapter à vos besoins, charger vos données, former un pipeline, l'exporter sous forme de package Python, télécharger vos résultats vers un stockage distant et partager vos résultats avec votre équipe.

## Présentation du projet ner_demo_expand
Dans ce repo, vous trouverez le projet ner_demo_expand, qui est une adaptation du projet [pipelines/ner_demo_replace](https://github.com/explosion/projects/tree/v3/pipelines/ner_demo_replace). Ce dernier rajoute un modèle de type NER à un pipeline qui fait déjà de la NER, sans écraser le modèle préexistant.

En effet, [Ines Montari](https://ines.io/) explique en réponse à un post intitulé [Adding a custom NER to a pipeline overrides an original NER](https://support.prodi.gy/t/adding-a-custom-ner-to-a-pipeline-overrides-an-original-ner/837): ["Le reconnaisseur d'entités de spaCy devrait respecter les entités prédéfinies, et il peut même améliorer les prédictions, puisque les entités que vous avez définies manuellement définiront les contraintes pour le reconnaisseur d'entités statistique."](https://support.prodi.gy/t/adding-a-custom-ner-to-a-pipeline-overrides-an-original-ner/837/2). Ce cas d'usage s'applique à une combinaison entre le reconnaisseur d'entités à base de règles [```EntityRuler```](https://spacy.io/api/entityruler) et le reconnaisseur d'entités statistique [```EntityRecognizer```](https://spacy.io/api/entityrecognizer). Ici, nous combinons 2 reconnaisseur d'entités statistique: 1 préentrainé qu'on ne change pas, + 1 qui sera réentrainé. Ainsi, théoriquement le second devrait tenir compte des annotations du premier pour extraire des entités. Il faut cependant noter qu'il n'est pas possible de re-typer une entité, car l'overlap est interdit dans Spacy.

## Packaging avec [Poetry](https://python-poetry.org/)
Ce projet utilise Poetry pour la gestion des dépendances. Pour installer Poetry, le plus simple c'est de lancer la commande ```pip install poetry```. Veuillez consulter [la doc en ligne](https://python-poetry.org/) pour une installation plus adaptée à votre environnement.

### Installer les dépendances
- Lancer la commande ```poetry install``` lancera l'installation des packages définis dans le fichier pyproject.toml

### Activer l'environnement
- ```poetry shell``` activera l'environnement du projet
- Rendez-vous ensuite dans le dossier ner_demo_expand (```cd ner_demo_expand```) pour commencer à utiliser les commandes du projet.