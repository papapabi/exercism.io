import string


_ALPHABET = string.ascii_lowercase
_DIGITS = string.digits
ATBASH_ALPHABET = string.ascii_lowercase[::-1]
ENCODING = {chr:enc for chr, enc in zip(_ALPHABET, ATBASH_ALPHABET)}
DECODING = {chr:dec for chr, dec in zip(ATBASH_ALPHABET, _ALPHABET)}


def encode(plain_text, group_size=5):
    encoding_chars = []
    for c in plain_text.lower():
        if c in _ALPHABET:
            encoding_chars.append(ENCODING[c])
        elif c in _DIGITS:
            encoding_chars.append(c)
        else:
            # We're only concerned with alphanumeric characters.
            # Everything else is thrown away.
            continue
    encoding = ''.join(encoding_chars) # Prior to being separated
    return ' '.join(encoding[i:i+group_size] for i in range(0, len(encoding),
                                                            group_size))

def decode(cipher_text):
    decoding_chars = []
    for c in cipher_text.lower():
        if c in ATBASH_ALPHABET:
            decoding_chars.append(DECODING[c])
        elif c in _DIGITS:
            decoding_chars.append(c)
        else:
            continue
    decoding = ''.join(decoding_chars)
    return ''.join(decoding)
