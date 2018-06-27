from collections import Counter

def yacht_fun(dice):
    c = Counter(dice)
    if len(c) == 1:
        return 50
    else:
        return 0

def four_of_a_kind(dice):
    c = Counter(dice)
    number, count = c.most_common(1)[0]
    if len(c) <= 2 and count >= 4: # Could be a Yacht or a Four-of-a-kind.
        return number * 4
    else:
        return 0

def full_house(dice):
    c = Counter(dice)
    number, count = c.most_common(1)[0]
    if len(c) == 2 and count == 3: # No other condition suffices.
        return sum(dice)
    else:
        return 0

def count_fun(num):
    return lambda dice: num * Counter(dice)[num]

def little_straight(dice):
    return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0

def big_straight(dice):
    return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0

YACHT = yacht_fun
ONES = count_fun(1)
TWOS = count_fun(2)
THREES = count_fun(3)
FOURS = count_fun(4)
FIVES = count_fun(5)
SIXES = count_fun(6)
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = sum

def score(dice, category):
    return category(dice)
