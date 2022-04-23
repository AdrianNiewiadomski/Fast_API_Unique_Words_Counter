import unittest

from main import remove_punctuation_symbols, count_unique_words


class TestClass(unittest.TestCase):
    def test_remove_punctuation_symbols(self):
        text_with_punctuation = "Live and learn? Learn and live!"
        text_without_punctuation = "Live and learn Learn and live"
        self.assertEqual(
            remove_punctuation_symbols(text_with_punctuation),
            text_without_punctuation
        )

    def test_count_unique_words(self):
        text_without_punctuation = "Live and learn Learn and live"
        self.assertEqual(count_unique_words(text_without_punctuation), 3)
