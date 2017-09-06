def is_isogram(string):
    orig = list(string.lower())
    for letter in orig:
        if letter.isalpha():
            if orig.count(letter) > 1:
                return False
            else:
                continue
    return True
