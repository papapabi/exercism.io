import re
import secrets
import string
from itertools import cycle

ALPHABET = string.ascii_lowercase
ALPHABET_MAPPING = {key: index for index, key in
                    enumerate(ALPHABET)}

INVALID_CHARACTERS_REGEX = re.compile(r'[^a-z]')

def shift_char(letter, key, reverse=False):
    orig = ALPHABET_MAPPING[letter]
    shift_amount = ALPHABET_MAPPING[key]
    if reverse:
        shift_amount = -shift_amount
    result_letter = (orig + shift_amount) % 26
    return chr(result_letter + 97) # 'a' is 97 in ASCII.

def has_invalid_chars(key):
    return INVALID_CHARACTERS_REGEX.search(key) or key.strip() == ''

class Cipher(object):
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(secrets.choice(ALPHABET) for i in range(100))
        else:
            if has_invalid_chars(key):
                raise ValueError(f"only lowercase ascii letters are allowed for\
                                 the key. key: {key}")
            self.key = key

    def encode(self, plaintext):
        return ''.join(shift_char(p, k) for p, k in
                       zip(plaintext, cycle(self.key)))

    def decode(self, ciphertext):
        return ''.join(shift_char(p, k, True) for p, k in
                       zip(ciphertext, cycle(self.key)))
