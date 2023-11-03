from typing import Union

from fastapi import FastAPI

app = FastAPI(title="NLP Server Back", summary="Derfulio's favorite app. Nuff said.", version="0.2.1")

@app.get("/")
async def read_root():
    return {"Allo Allo": "J'écoute!"}


@app.get("/health")
async def health_check():
    return {"statut": "Serveur OK"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
