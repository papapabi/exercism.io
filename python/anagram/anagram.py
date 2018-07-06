def detect_anagrams(word, candidates):
    return [w for w in candidates if is_anagram(w, word)]

def is_anagram(s1, s2):
    """Returns true if s1 and s2 are anagrams."""
    s1_l = s1.lower()
    s2_l = s2.lower()
    return (sorted(s1_l) == sorted(s2_l) and s1_l != s2_l)
