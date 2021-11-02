import re
from unittest import TestCase


seed_phrase_pattern = re.compile(r'^([a-zA-Z]|\s)+$')


class TestSeedPhrase(TestCase):
    def test_seed_phrase(self):
        from lib import seed_phrase
        generated_seed_phrase = seed_phrase.generate_curse_seed_phrase()
        print(generated_seed_phrase)
        self.assertEqual(len(generated_seed_phrase.split(" ")), 24)
        self.assertTrue(seed_phrase_pattern.match(generated_seed_phrase))


    def test_seed_phrase_length(self):
        from lib import seed_phrase
        generated_seed_phrase = seed_phrase.generate_curse_seed_phrase(12)
        self.assertEqual(len(generated_seed_phrase.split(" ")), 12)
        self.assertTrue(seed_phrase_pattern.match(generated_seed_phrase))
