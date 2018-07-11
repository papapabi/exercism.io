def sum_of_multiples(limit, numbers):
    if not numbers:
        return 0
    multiples = []
    for n in numbers:
        for i in range(n, limit, n):
            multiples.append(i)

    return sum(set(multiples))
