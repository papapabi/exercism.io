import re

def abbreviate(words):
    word_regex = re.compile(r'\b[0-9a-zA-Z]+')
    normalized_words = re.findall(word_regex, words)
    first_letters = (w[0] for w in normalized_words)
    return ''.join(first_letters).upper()
