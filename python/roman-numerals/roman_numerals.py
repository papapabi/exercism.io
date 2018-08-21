from bisect import bisect_right
from collections import OrderedDict
from itertools import count


# Those that can be repeated can be done so thrice max.
TO_ROMAN = [
    (1, 'I'), # can be repeated
    (4, 'IV'),
    (5, 'V'),
    (9, 'IX'),
    (10, 'X'), # can be repeated
    (40, 'XL'),
    (50, 'L'),
    (90, 'XC'),
    (100, 'C'), # can be repeated
    (400, 'CD'),
    (500, 'D'),
    (900, 'CM'),
    (1000, 'M') # can be repeated
]
TO_ROMAN = OrderedDict(TO_ROMAN)
_POSSIBLE_VALUES = list(TO_ROMAN.keys())


def numeral(n):
    """Convert integer n to its equivalent representation in Roman Numerals."""
    if n < 1:
        raise ValueError(
            f'roman numerals undefined for n < 1: roman_numerals({n})')

    numeral = ''

    for exp, val in zip(count(start=0, step=1), reversed(str(n))):
        val = int(val)
        if val == 0:
            continue
        place_value = 10**exp * val
        to_prepend = '' 
        while place_value > 0: # For repetitions; greedy algorithm
            key = _find_le_in_to_roman(place_value)
            to_prepend += TO_ROMAN[key]
            place_value -= key
        numeral = to_prepend + numeral

    return numeral


def _find_le_in_to_roman(n):
    """Return the rightmost numeral less than or equal to int n in TO_ROMAN."""
    return _find_le(_POSSIBLE_VALUES, n)


def _find_le(a, x):
    """Find rightmost value less than or equal to x."""
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError
