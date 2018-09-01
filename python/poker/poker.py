# There are 9 hand-ranking categories when using a standard 52-card deck.
# Use a histogram-based solution?
# Suits are apparently not ranked in poker.
# from collections import Counter
import re
from collections import Counter
from enum import Enum
from functools import total_ordering


CARD_REGEX = re.compile(r'(\d+)(\w)')


@total_ordering
class Card(object):
    _ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    RANKS = {rank: val for val, rank in enumerate(_ranks)}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "{classname}(rank={rank}, suit={suit})".format(
            classname = self.__class__.__name__,
            rank = self.rank,
            suit = self.suit)

    def __str__(self):
        return self.rank + self.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.RANKS[self.rank] < self.RANKS[other.rank]


class Combination(Enum):
    ROYAL_FLUSH = 9
    STRAIGHT_FLUSH = 8
    FOUR_OF_A_KIND = 7
    FULL_HOUSE = 6
    FLUSH = 5
    STRAIGHT = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    PAIR = 1
    HIGH_CARD = 0


def normalize(hand):
    """Return a reverse sorted list of Card instances."""
    cards = [Card(rank, suit) for rank, suit in CARD_REGEX.findall(hand)]
    return sorted(cards, reverse=True)

def generate_histogram(cards):
    """Return a histogram of card ranks as a counter."""
    return Counter(card.rank for card in cards)


def best_hands(hands):
    """Return the best poker hand(s) from a list of hands."""
    pass

