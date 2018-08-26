OPENING_BRACKETS = '({['
CLOSING_BRACKETS = ')}]'
MATCHING = {closing: opening for closing, opening in zip(CLOSING_BRACKETS,
                                                         OPENING_BRACKETS)}


def is_paired(s):
    """Return true if string s contains balanced parentheses."""
    stack = []
    for chr in s:
        if chr in OPENING_BRACKETS:
            stack.append(chr)
        elif chr in CLOSING_BRACKETS:
            try:
                opening_bracket = stack.pop()
            except IndexError: # stack is empty
                return False
            if opening_bracket != MATCHING[chr]:
                return False
    return not stack
