from functools import reduce
from operator import mul

def largest_product(series, size):
    if size < 0:
        raise ValueError("series length cannot be <= 0")
    products = []
    subsequences = (cons for cons in each_cons(series, size))
    for subsequence in subsequences:
        digits = (int(c) for c in subsequence)
        products.append(reduce(mul, digits, 1))
    return max(products)

def each_cons(xs, size):
    return (xs[i:i+size] for i in range(len(xs)-size+1))
