import string, re

def is_pangram(phrase):
    pattern = re.compile('[\W_]+')
    normalized_phrase = pattern.sub('', phrase).lower()
    return not (set(string.ascii_lowercase) - set(normalized_phrase))


