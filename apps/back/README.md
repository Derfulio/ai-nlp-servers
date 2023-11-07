# Serveur BACK

***Source: https://medium.com/@caetanoog/start-your-first-fastapi-server-with-poetry-in-10-minutes-fef90e9604d9***

## Poetry usefull commands

- ```poetry new back``` --> Crée le dossier du projet
- ```poetry install``` --> installe les packages dans la VM du projet (rq: se positionner dans le repo du projet pour que cela fonctionne.)

### Create it
***https://fastapi.tiangolo.com/#create-it***
- ```poetry add fastapi uvicorn[standard]``` --> Ajout des librairies basiques pour utiliser FastAPI

### Run it
***https://fastapi.tiangolo.com/#run-it***
- ```poetry shell``` --> Activation de l'environnement virtuel
- ```cd back``` --> on va dans le répertoire du serveur
- ```uvicorn main:app --reload``` --> on active le serveur

### Test it
***https://fastapi.tiangolo.com/tutorial/testing/***
- ```poetry add pytest --group test``` --> nécessaire pour les tests unitaires
- ```poetry add httpx --group test``` --> nécessaire pour les tests unitaires fastapi
- ```poetry run pytest``` --> lance les tests unitaires

### Check it
***https://fastapi.tiangolo.com/#check-it***
- Clicker sur http://127.0.0.1:8000/health 
- JSON attendu: {"statut":"Serveur OK"}

### Clean it
- ```poetry add black --group dev``` --> Formatteur de code python
- ```poetry run black back``` --> Check que tous les fichiers python sont correctement formatés

## Container
### Image specks
- Base Python 3.11 sur Alipne3.18 pour la taille (3.11.6-alpine3.18). On précise les numéros de version pour avoir une image très précise
- RQ: On pourrait vouloir se créer une image python avec Poetry commune aux différents serveurs du projet, pour plus d'efficacité. A voir comment partager une image de base sans la publier dans le hub docker, par exemple dans le répertoire Apps/images

### Build it
```docker build -t nlp-server-back .```

### Run it
```docker run -d --name nlp-server -p 8000:80 nlp-server-back```
***Ici le port 8000 est le port sur ma machine, et le port 80 est le port dans le container.***

### Check it
***https://fastapi.tiangolo.com/#check-it***
- Clicker sur http://127.0.0.1:8000/health 
- JSON attendu: {"statut":"Serveur OK"}
- API disponible ici: http://localhost:8000/docs

## Spacy Integration
Ce serveur va utiliser Spacy pour orchestrer les workflows d'analyse NLP.
Inspiré de l'exemple d'intégration de projects/integrations/fastapi que l'on peut trouver sur le GitHub d'Explosion: https://github.com/explosion/projects/tree/v3/integrations/fastapi.

