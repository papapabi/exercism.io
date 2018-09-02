import operator
import re
from collections import Counter
from enum import IntFlag
from functools import total_ordering


CARD_REGEX = re.compile(r'(\d+|\w)(\w)')


class Combination(IntFlag):
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


@total_ordering
class Card(object):
    _ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    RANKS = {rank: val for val, rank in enumerate(_ranks)}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "{classname}(rank='{rank}', suit='{suit}')".format(
            classname = self.__class__.__name__,
            rank = self.rank,
            suit = self.suit)

    def __str__(self):
        return self.rank + self.suit

    def __eq__(self, other):
        """In the context of poker, suits are irrelevant for comparison."""
        return self.rank == other.rank

    def __lt__(self, other):
        return self.numeric_rank < other.numeric_rank

    @property
    def numeric_rank(self):
        return self.RANKS[self.rank]


@total_ordering
class Hand(object):
    def __init__(self, str):
        """hand: str"""
        cards = _str_to_cards(str)
        self.cards = _normalize(cards)

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score
    
    @property
    def combination(self):
        return _find_combination(self.cards)

    @property
    def score(self):
        return _score_hand(self.combination, self.cards)


def _str_to_cards(hand_str):
    """Return a list of cards from a hand as a string."""
    return [Card(rank, suit) for rank, suit in CARD_REGEX.findall(hand_str)]

def _normalize(cards):
    """Normalize a group of cards."""
    sort_by_rank = sorted(cards, reverse=True)
    return sorted(sort_by_rank, key=lambda x: sort_by_rank.count(x),
                  reverse=True)

def _generate_rank_histogram(cards):
    """Return a histogram of card ranks as a Counter."""
    return Counter(card.rank for card in cards)

def _generate_suit_histogram(cards):
    """Return a histogram of card suits as a Counter."""
    return Counter(card.suit for card in cards)

def _find_combination(cards):
    """Find the combination of a hand's cards."""

    # Flags for a flush and a straight.
    flush = False
    straight = False

    rank_counts = [count for _, count in
                   _generate_rank_histogram(cards).most_common()]
    if 4 in rank_counts:
        return Combination.FOUR_OF_A_KIND
    elif 3 in rank_counts and 2 in rank_counts:
        return Combination.FULL_HOUSE
    elif 3 in rank_counts and rank_counts.count(1) == 2:
        return Combination.THREE_OF_A_KIND
    elif rank_counts.count(2) == 2:
        return Combination.TWO_PAIR
    elif 2 in rank_counts:
        return Combination.PAIR

    suit_counts = [count for _, count in
                   _generate_suit_histogram(cards).most_common()]
    if len(suit_counts) == 1:
        flush = True

    if cards[0].numeric_rank - cards[-1].numeric_rank == 4:
        straight = True
    elif cards[0].numeric_rank == 12 and cards[1].numeric_rank == 3:
        straight = True # A wheel (ace to 5 straight).

    if flush and straight:
        if cards[0].numeric_rank == 12: # The highest card is an Ace.
            return Combination.ROYAL_FLUSH
        else:
            return Combination.STRAIGHT_FLUSH
    elif flush:
        return Combination.FLUSH
    elif straight:
        return Combination.STRAIGHT
    # If we still haven't matched anything, it's a High Card.
    return Combination.HIGH_CARD

def _score_hand(combination, cards):
    """Score a hand given its combination and list of Card instances."""
    score = combination
    for card in cards:
        score = (score << 4) + card.numeric_rank
    return score

def best_hands(hands):
    """Return the best poker hand(s) from a list of hands."""
    hands_instances = [Hand(hand_str) for hand_str in hands]
    max_score = max(hands_instances).score
    return [hands[index] for index, hand in enumerate(hands_instances) if
            hand.score == max_score]
