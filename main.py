from fastapi import Request, FastAPI

from unique_words_counter import UniqueWordsCounter

app = FastAPI()


@app.post("/words")
async def root(request: Request):
    data: dict = await request.json()
    uwc = UniqueWordsCounter(data["text"])
    data["uniqueWordsCount"] = uwc.analyze_data()
    return data
