from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
import time

from db import models
from db.database import engine, SessionLocal
from unique_words_counter import UniqueWordsCounter
from db.models import RequestTexts

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class WordsRequest(BaseModel):
    text: str


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/words")
async def root(words_request: WordsRequest, db: Session = Depends(get_db)):
    data = {"text": words_request.text}

    uwc = UniqueWordsCounter(data["text"])
    data["uniqueWordsCount"] = uwc.analyze_data()

    rt = RequestTexts()
    rt.creation_timestamp = datetime.fromtimestamp(time.time())
    rt.text = data["text"]
    rt.unique_words_count = data["uniqueWordsCount"]

    db.add(rt)
    db.commit()

    return data


@app.get("/words")
def fetch_data():
    db = SessionLocal()
    return tuple(db.query(RequestTexts).all())
