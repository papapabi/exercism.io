from functools import reduce
from math import sqrt

def classify(n):
    if n <= 0:
        raise ValueError("n <= 0 no factors")
    aliquot_sum = sum(factors_not_including(n))
    if aliquot_sum == n:
        return "perfect"
    elif aliquot_sum > n:
        return "abundant"
    else:
        return "deficient"

def factors_not_including(n):
    factors = set(
        reduce(list.__add__, [[i, n//i] for i in range(1, int(sqrt(n))+1)
                              if n % i == 0]))
    factors.remove(max(factors))
    return factors
