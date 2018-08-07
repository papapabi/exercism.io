import re
from itertools import zip_longest
from math import ceil, sqrt


INVALID_CHAR_REGEX = re.compile(r'[^a-zA-Z0-9]*')


def _normalize(s):
    """Returns a downcased string with all spaces and punctuation removed."""
    spaces_punct_removed = INVALID_CHAR_REGEX.sub('', s)
    return spaces_punct_removed.lower()


def _find_c(area):
    """Returns the width of a rectangle (# of cols)."""
    return ceil(sqrt(area))


def _grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks, filling if needed."""
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def encode(plain_text):
    normalized_plain_text = _normalize(plain_text)
    area_of_rect = len(normalized_plain_text)
    c = _find_c(area_of_rect)

    chunks_of_length_c = _grouper(normalized_plain_text, c, ' ')

    iter_ciphertext = (''.join(chunk) for chunk in zip(*chunks_of_length_c))

    return ' '.join(iter_ciphertext)
