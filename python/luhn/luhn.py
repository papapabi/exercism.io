import itertools
import re

WHITESPACE_REGEX = re.compile(r'\s')
INVALID_CHARS = re.compile(r'[^\d]')

def is_valid_card_num(card_num):
    """Returns true if the card number is syntactically valid.

    Grounds for validity:
        a) length of the card number must be greater than 1
        b) there must be no other characters save for digits
    """
    card_num = normalize(card_num) # Removes whitespace.
    return not INVALID_CHARS.search(card_num) and len(card_num) > 1

def normalize(card_num):
    """Removes all whitespace from the card number."""
    return re.sub(WHITESPACE_REGEX, '', card_num)

def luhn_logic(digit):
    digit = int(digit) * 2
    if digit > 9:
        digit = digit - 9
    return str(digit)

class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num

    def is_valid(self):
        if not is_valid_card_num(self.card_num):
            return False
        card_num = normalize(self.card_num) # Remove whitespaces from card_num.
        card_num_reversed = card_num[::-1]
        # Perform the first step of the Luhn algorithm for every 2nd digit
        # from the right.
        luhn_step = map(luhn_logic, card_num_reversed[1::2])
        other_digits = card_num_reversed[::2]
        sum_of_digits = sum(int(i)
                            for i in itertools.chain(luhn_step, other_digits))
        return sum_of_digits % 10 == 0
