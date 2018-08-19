import re
from collections import Counter


def is_isogram(s):
    if not s:
        return True # The empty string is an isogram by definition.
    s = s.lower()
    s = re.sub(r'[^A-Za-z]', '', s) # Remove all non-alphabetic characters.
    # counter.most_common([n]) returns a list of 2-tuples of the elements and
    # their corresponding counts.
    return Counter(s).most_common(1)[0][1] == 1
