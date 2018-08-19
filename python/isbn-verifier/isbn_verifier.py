import re


ISBN_REGEX = re.compile('[0-9]{9}[0-9Xx]')


def verify(isbn):
    isbn = isbn.replace('-', '') # Remove hyphens from the string, if it has.
    if len(isbn) != 10:
        return False
    if not valid_isbn_characters(isbn):
        return False

    # Get product up to (but not including) the last char in the ISBN string.
    products = [int(isbn_digit) * multiplier for isbn_digit, multiplier
                in zip(isbn[:-1], range(10, 0, -1))]

    # The last char is either a digit or X, append the appropriate value.
    products.append(int(isbn[-1]) if isbn[-1].isdigit() else 10)

    return sum(products) % 11 == 0


def valid_isbn_characters(isbn):
    """Returns true if the given string matches the ISBN-10 format."""
    return ISBN_REGEX.match(isbn)
