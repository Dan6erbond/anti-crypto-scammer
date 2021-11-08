import random
import re

from better_profanity.utils import get_complete_path_of_file, read_wordlist

phrase_lengths_to_strength = {
    12: 128,
    24: 256,
}

word_pattern = re.compile(r'^[a-zA-Z]+$')
curse_word_list = [word for word in read_wordlist(
    get_complete_path_of_file("profanity_wordlist.txt")) if word_pattern.match(word)]


def generate_curse_seed_phrase(length: int = 24) -> str:
    """
    Generate a random seed phrase using cursewords.
    """
    seed_phrase = []
    for _ in range(length):
        seed_phrase.append(curse_word_list[int(len(curse_word_list) * random.random())])
    return " ".join(seed_phrase)
