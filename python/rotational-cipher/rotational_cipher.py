import string

def rotate(text, key):
    ALPHABET_INDEX = { char: index for index, char in
                      enumerate(string.ascii_lowercase) }
    cipher_alphabet = __generate_cipher_alphabet(key)
    cipher_chars = []

    for char in text:
        cipher_char = char
        if char.isalpha():
            cipher_char = cipher_alphabet[ALPHABET_INDEX[char.lower()]]
            if char.isupper():
                cipher_char = cipher_char.upper()
        cipher_chars.append(cipher_char)

    return ''.join(cipher_chars)

def __generate_cipher_alphabet(n):
    """Generates a rotational cipher alphabet given key n.

    """
    return string.ascii_lowercase[n:] + string.ascii_lowercase[:n]
