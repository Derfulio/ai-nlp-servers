from typing import List, Dict, Any
from enum import Enum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import spacy
from spacy.tokens import Doc


class ModelName(str, Enum):
    # Enum of the available models. This allows the API to raise a more specific
    # error if an invalid model is provided.
    fr_core_news_sm = "fr_core_news_sm"
    fr_core_news_md = "fr_core_news_md"
    fr_core_news_lg = "fr_core_news_lg"
    fr_dep_news_trf = "fr_dep_news_trf"
    xx_ent_wiki_sm = "xx_ent_wiki_sm"
    xx_sent_ud_sm = "xx_sent_ud_sm"


DEFAULT_MODEL = ModelName.fr_core_news_sm
MODEL_NAMES = [model.value for model in ModelName]
MODELS = {name: spacy.load(name) for name in MODEL_NAMES}
print(f"Loaded {len(MODEL_NAMES)} models: {MODEL_NAMES}")


class Article(BaseModel):
    # Schema for a single article in a batch of articles to process
    text: str


class RequestModel(BaseModel):
    articles: List[Article]
    model: ModelName = DEFAULT_MODEL


class ResponseModel(BaseModel):
    # This is the schema of the expected response and depends on what you
    # return from get_data.

    class Batch(BaseModel):
        class Entity(BaseModel):
            text: str
            label: str
            start: int
            end: int

        text: str
        ents: List[Entity] = []

    result: List[Batch]


def get_data(doc: Doc) -> Dict[str, Any]:
    """Extract the data to return from the REST API given a Doc object. Modify
    this function to include other data."""
    ents = [
        {
            "text": ent.text,
            "label": ent.label_,
            "start": ent.start_char,
            "end": ent.end_char,
        }
        for ent in doc.ents
    ]
    return {"text": doc.text, "ents": ents}


# Set up the FastAPI app and define the endpoints
app = FastAPI(
    title="NLP Server Back",
    summary="Derfulio's favorite app. Nuff said.",
    version="0.2.1",
)
app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.get("/")
async def read_root():
    return {"Allo Allo": "J'écoute!"}


@app.get("/health")
async def health_check():
    return {"statut": "Serveur OK"}


@app.get("/models", summary="List all loaded models")
def get_models() -> List[str]:
    """Return a list of all available loaded models."""
    return MODEL_NAMES


@app.post("/process/", summary="Process batches of text", response_model=ResponseModel)
def process_articles(query: RequestModel):
    """Process a batch of articles and return the entities predicted by the
    given model. Each record in the data should have a key "text".
    """
    nlp = MODELS[query.model]
    response_body = []
    texts = (article.text for article in query.articles)
    for doc in nlp.pipe(texts):
        response_body.append(get_data(doc))
    return {"result": response_body}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#   return {"item_id": item_id, "q": q}
