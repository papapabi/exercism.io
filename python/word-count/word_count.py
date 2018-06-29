import re
from collections import Counter

word_regex = re.compile(r"(?<![@#])[A-Za-z0-9]+(?:'[A-Za-z0-9]+)?")

def word_count(phrase):
    words = re.findall(word_regex, phrase.lower())
    occurrences = Counter(words)
    return occurrences
