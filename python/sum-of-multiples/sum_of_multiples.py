def sum_of_multiples(limit, numbers):
    if not numbers:
        return 0
    multiples = set()
    for n in numbers:
        for i in range(n, limit, n):
            multiples.add(i)

    return sum(multiples)
