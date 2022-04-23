class UniqueWordsCounter:
    def __init__(self, text: str):
        self.text = text

    def analyze_data(self) -> int:
        self.text = self.text.replace("\n", " ")
        self._remove_punctuation_symbols()
        return self._count_unique_words()

    def _remove_punctuation_symbols(self) -> None:
        punctuation_symbols = [",", ".", ":", "?", "!"]

        for symbol in punctuation_symbols:
            self.text = self.text.replace(symbol, "")

    def _count_unique_words(self) -> int:
        self.text = self.text.upper()
        unique_words = set(self.text.split())
        return len(unique_words)
