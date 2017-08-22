import random

from unittest import TestCase
from  quotify.quote_generator import Quotify

class TestQuotify(TestCase):

    def setUp(self):
        self.quotify = Quotify()

    def test_get_file_contents(self):

        file_content = self.quotify.get_file_contents("resources/quotes.txt")
        self.assertEqual(len(file_content),19)
        self.assertEqual(file_content[0],"\"If you want to shine like a sun. First burn like a sun.\"\n")

    def test_get_quote(self):
        quotes = ["a","b","c","d","e","f","g","h","i","j"]
        seed = 5
        random_quote = self.quotify.get_quote(quotes,seed)
        random.seed(seed)
        self.assertEqual(random.choice(quotes),random_quote)
