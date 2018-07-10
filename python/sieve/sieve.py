from itertools import compress
from math import ceil, sqrt

def sieve(n):
    """Generate primes up to (and including) n."""
    numbers = range(n + 1)
    # is_prime is a list of selectors with the number's primality (true
    # for prime, false if otherwise) indexed by the number in question.
    # 0 and 1 are non-prime, and everything else is assumed to be a prime until
    # they are marked off.
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, ceil(sqrt(n))):
        if is_prime[i]:
            # Mark all multiples of the current prime, as they are composite.
            is_prime[i*2::i] = [False] * len(is_prime[i*2::i])

    return list(compress(numbers, is_prime))
