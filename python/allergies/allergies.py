import math

class Allergies(object):
    allergens = ["cats", "pollen", "chocolate", "tomatoes", "strawberries",
                 "shellfish", "peanuts", "eggs"]
    allergen_scores = [2**i for i in reversed(range(len(allergens)))]
    MAX_ALLERGEN_SCORE = 2**len(allergens)

    def __init__(self, score):
        self.score = score
        score = self._reduce_until_max_allergen(score)
        self._lst = []
        for index, allergen_score in enumerate(self.allergen_scores):
            if score - allergen_score >= 0:
                self._lst.append(self.allergens[index])
                score -= allergen_score

    def is_allergic_to(self, item):
        return item in self._lst

    def _reduce_until_max_allergen(self, n):
        if n <= 256:
            return n
        return n % self.MAX_ALLERGEN_SCORE

    @property
    def lst(self):
        return self._lst
