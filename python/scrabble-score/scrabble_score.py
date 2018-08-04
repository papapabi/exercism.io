letters = 'aeioulnrstdgbcmpfhvwykjxqz'
values = '111111111122333344444588aa'
scrabble_mapping = str.maketrans(letters, values)

def score(word):
    return sum(int(score, 11) for score in word.lower()
               .translate(scrabble_mapping))
