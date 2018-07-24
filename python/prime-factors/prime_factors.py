def prime_factors(n):
    prime_factors = []
    candidate = 2
    while n > 1:
        if n % candidate == 0:
            prime_factors.append(candidate)
            n //= candidate
        else:
            candidate += 1
    return prime_factors
