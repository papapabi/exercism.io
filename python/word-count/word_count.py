import re

word_regex = re.compile(r"(?<![@#])\b[A-Za-z0-9]+(?:'[A-Za-z0-9]+)?")

def word_count(phrase):
    occurrences = {}
    words = re.findall(word_regex, phrase.lower())
    for word in words:
        occurrences[word] = occurrences.get(word, 0) + 1
    return occurrences
