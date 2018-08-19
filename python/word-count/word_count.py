import re
from collections import Counter


def word_count(phrase):
    words = [word.strip("'") for word in
             re.findall(r'[a-z\d]*\'?[a-z\d]+', phrase.lower())]
    return Counter(words)
