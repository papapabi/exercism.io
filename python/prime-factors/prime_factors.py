def prime_factors(n):
    prime_factors = []
    if n == 1:
        return prime_factors
    i = 2
    while n > 1:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    return prime_factors
