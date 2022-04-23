from fastapi import Request, FastAPI

app = FastAPI()


def remove_punctuation_symbols(text: str) -> str:
    punctuation_symbols = [",", ".", ":", "?", "!"]

    for symbol in punctuation_symbols:
        text = text.replace(symbol, "")

    return text


def count_unique_words(text: str) -> int:
    text = text.upper()
    unique_words = set(text.split())
    print("unique_words: ", unique_words)
    return len(unique_words)


def analyze_data(text: str):
    print("text: ", text)
    text = text.replace("\n", " ")
    text = remove_punctuation_symbols(text)
    number_of_unique_words = count_unique_words(text)
    return number_of_unique_words


@app.post("/words")
async def root(request: Request):
    data: dict = await request.json()
    data["uniqueWordsCount"] = analyze_data(data["text"])
    return data
