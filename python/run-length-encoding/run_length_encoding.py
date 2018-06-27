import re
from itertools import groupby

def decode(s):
    occurrences_and_char = re.findall('(\d+)*(.)', s)
    decoding_chars = []
    for num, char in occurrences_and_char:
        if num:
            decoding_chars.append(int(num) * char)
        else:
            decoding_chars.append(char)
    return ''.join(decoding_chars)

def encode(s):
    encoding_chars = []

    for char, char_grouper in groupby(s):
        char_group = list(char_grouper)
        if len(char_group) == 1:
            num = ""
        else:
            num = str(len(char_group))
        encoding_chars.append(num + char)

    return ''.join(encoding_chars)
