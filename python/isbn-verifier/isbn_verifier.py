import re

def verify(isbn):
    normalized_isbn = normalize(isbn)
    isbn_length = len(normalized_isbn)
    if isbn_length != 10:
        return False
    if not is_valid_isbn_characters(normalized_isbn):
        return False
    multiplicand = 10
    value = 0
    normalized_isbn_integers = [int(x) if x.isdigit() else 10 for x in
                                normalized_isbn]
    for integer in normalized_isbn_integers:
        value += integer*multiplicand
        multiplicand -= 1

    return (value % 11 == 0)

def normalize(isbn):
    """Remove dashes from the string, if it has.
    """
    return isbn.replace("-", "")

def is_valid_isbn_characters(isbn):
    """Check if given string matches the isbn pattern.
    """
    regex = re.compile('[0-9]{9}[0-9X]')
    return bool(regex.search(isbn))
