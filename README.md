# ai-nlp-servers

**Bon. En résumé on veut faire quoi?**

## Etape 0
### Arborescence du projet
ai-nlp-servers
	- LICENSE
	- README.md
	- .gitignore
	- apps
		- back
		- front
			- demo
			- annotation
		- notebooks

### Choix techniques
J'ai choisi d'utiliser les technologies suivantes:
- GitHub : (https://github.com) Pour le versionning et pourquoi pas la mise en place d'une chaine CI/CD
- Docker : (https://www.docker.com/) Pour la reproductibilité, plus simple pour distribuer mes serveurs.
- Poetry : (https://python-poetry.org/) Pour la gestion des dépendances et le packaging.
- Spacy : (https://spacy.io/) Librairie NLP à utiliser afin de servir de POC. "spacy[cuda12x,transformers,lookups]", devra être installé sur chaque serveur.
- FastAPI: (https://fastapi.tiangolo.com/) Librairie permettant la conception de serveurs compatibles OpenAPI (https://www.openapis.org/)
- StreamLit: (https://streamlit.io/) Librairie permettant de concevoir des UI simples rapidement, idéal pour servir de FRONT de démo.
- VSCode: pour concevoir un environnement de développement contenairisé, qui sera mon livrable en fin de projet.

## Etape 1
Je veux concevoir 3 serveurs pour commencer: 
- 1 BACK avec fastapi
- 1 FRONT avec streamlite:
	Il appellera le serveur fastapi. Devra rester simple afin de servir de démo.
- 1 JupiterLab pour faire des tests:
	Tout ce que je n'aurai pas su faire dans le serveur se fera là. Pour le moment il ne contiendra rien de particulier, si ce n'est une reprise de mes travaux précédents.

## Etape 2
Je veux tester les capacités d'apprentissage de Spacy. Conception d'un workflow d'apprentissage et de génération de modèle. On utilisera le Jupiter notebook pour expérimenter.

## Etape 3
Je veux créer un serveur d'annotation. Je dois choisir entre:
	- Doccano: https://doccano.herokuapp.com/ --> Multipurpose annotation tool
	- Argilla: https://argilla.io/ --> NLP/LLM annotation tool
	- Label Studio : https://labelstud.io/ --> Multipurpose annotation tool
Pourquoi ces trois-là? Parce qu'il faut bien commencer quelque part. J'ai déjà testé doccano: j'ai eu du mal à le faire fonctionner avec Spacy. Argilla m'a été conseillé par des anciens collègues qui l'utilisent pour customiser des llms. Le dernier Label Studio reviens souvent dans mes recherches.

Quoi qu'il arrive, le workflow sera le suivant à cette étape:
	- Import d'un corpus de documents, format à définir.
	- Annotation du corpus.
	- Génération du corpus d'apprentissage et du corpus de test/dev.
	- Export et formatage des corpus au format attendu par Spacy pour l'apprentissage.

## Etape 4
Soyons fous: pourquoi pas implémenter une boucle de feedback? Faire de l'Active Learning?