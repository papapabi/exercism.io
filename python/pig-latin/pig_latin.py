import re


CONSONANT_CLUSTER_REGEX = re.compile(r'''
(
[^aeiou]+             # consonant cluster
(?: (?<=q) u)?        # qu rule
)                     # whole thing is group 1
(\w*)                 # the rest of the word, group 2
''', re.VERBOSE)


Y_RULE_REGEX = re.compile(r'''
([^aeiou]+)(?=y) # the consonant cluster up to (but not incl. y)
(\w*)            # the rest of the word, including y
''', re.VERBOSE)


VOWEL_SOUNDS = ('a', 'e', 'i', 'o', 'u', 'xr', 'yt')


def translate(text):
    translations = (translate_word(word) for word in text.split())
    return ' '.join(translations)


def translate_word(word):
    """Returns the pig latin translation of a word.

    Limitations: how about words like 'European', or 'hour'?
    """
    translation = word
    # Pre-emptively handle beginning consonants that sound like vowels.
    if word.startswith(VOWEL_SOUNDS):
        pass
    else:
        consonant_match = CONSONANT_CLUSTER_REGEX.match(word)
        y_rule_match = Y_RULE_REGEX.match(word)

        if consonant_match:
            translation = consonant_match.group(2) + consonant_match.group(1)
            # Special rule for cluster + y.
            if y_rule_match:
                translation = y_rule_match.group(2) + y_rule_match.group(1)

    # -ay is added to all words regardless of the rule applied.
    translation += 'ay'
    return translation
