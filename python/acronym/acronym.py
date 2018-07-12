import re

def abbreviate(words):
    return ''.join(_first_letters(words)).upper()

def _first_letters(words):
    first_letters = re.compile(r'\b[0-9a-zA-Z]')
    return re.findall(first_letters, words)
