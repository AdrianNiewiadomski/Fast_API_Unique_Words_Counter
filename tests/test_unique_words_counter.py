import unittest

from unique_words_counter import UniqueWordsCounter


class TestUniqueWordsCounter(unittest.TestCase):
    def test_remove_punctuation_symbols(self):
        uwc = UniqueWordsCounter("Live and learn? Learn and live!")
        uwc._remove_punctuation_symbols()
        text_without_punctuation = "Live and learn Learn and live"
        self.assertEqual(
            uwc.text,
            text_without_punctuation
        )

    def test_count_unique_words(self):
        uwc = UniqueWordsCounter("Live and learn Learn and live")
        self.assertEqual(uwc._count_unique_words(), 3)

    def test_analyze_data(self):
        uwc = UniqueWordsCounter("Live and learn? Learn and live!")
        self.assertEqual(uwc.analyze_data(), 3)
