from fastapi import Request, FastAPI
from sqlalchemy.orm import Session

import models
from database import engine
from unique_words_counter import UniqueWordsCounter

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post("/words")
async def root(request: Request):
    data: dict = await request.json()
    uwc = UniqueWordsCounter(data["text"])
    data["uniqueWordsCount"] = uwc.analyze_data()
    return data
