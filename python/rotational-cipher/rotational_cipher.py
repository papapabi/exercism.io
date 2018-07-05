import string

def rotate(text, key):
    plaintext_alphabet = string.ascii_lowercase
    ciphertext_alphabet = plaintext_alphabet[key:] + plaintext_alphabet[:key]
    cipher_table = str.maketrans(plaintext_alphabet 
                                 + plaintext_alphabet.upper(),
                                 ciphertext_alphabet 
                                 + ciphertext_alphabet.upper())
    return text.translate(cipher_table)
