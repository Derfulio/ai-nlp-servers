# Serveur BACK

***Source: https://medium.com/@caetanoog/start-your-first-fastapi-server-with-poetry-in-10-minutes-fef90e9604d9***

## Poetry usefull commands

- poetry new back --> Crée le dossier du projet

### Create it
***https://fastapi.tiangolo.com/#create-it***
- poetry add fastapi uvicorn[standard] --> Ajout des librairies basiques pour utiliser FastAPI

### Run it
***https://fastapi.tiangolo.com/#run-it***
- poetry shell --> Activation de l'environnement virtuel
- cd back --> on va dans le répertoire du serveur
- uvicorn main:app —-reload --> on active le serveur

### Test it
***https://fastapi.tiangolo.com/tutorial/testing/***
- poetry add pytest --group test --> nécessaire pour les tests unitaires
- poetry add httpx --group test --> nécessaire pour les tests unitaires fastapi
- poetry run pytest --> lance les tests unitaires

### Check it
***https://fastapi.tiangolo.com/#check-it***
- Clicker sur http://127.0.0.1:8000/health 
- JSON attendu: {"statut":"Serveur OK"}

### Clean it
- poetry add black --group dev --> Formatteur de code python
- poetry run black back --> Check que tous les fichiers python sont correctement formatés