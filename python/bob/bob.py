import re

RESPONSES = {'yelling': 'Whoa, chill out!',
             'question': 'Sure.',
             'yell_question': "Calm down, I know what I'm doing!",
             'silence': 'Fine. Be that way!',
             'default': 'Whatever.'}

def hey(phrase):
    n_phrase = normalize(phrase)
    if is_empty(n_phrase):
        return RESPONSES['silence']
    elif is_yelling_question(n_phrase):
        return RESPONSES['yell_question']
    elif is_yelling(n_phrase):
        return RESPONSES['yelling']
    elif is_question(n_phrase):
        return RESPONSES['question']
    else:
        return RESPONSES['default']

def normalize(phrase):
    # Replace all other forms of whitespace with a single space.
    n_phrase = re.sub(r'\s+', ' ', phrase)
    return n_phrase.strip()

def is_empty(phrase):
    return not phrase # Empty sequences evaluate to false.

def is_yelling(phrase):
    return phrase.upper() == phrase and phrase.lower() != phrase

def is_question(phrase):
    return phrase.endswith("?")

def is_yelling_question(phrase):
    return is_yelling(phrase) and is_question(phrase)
