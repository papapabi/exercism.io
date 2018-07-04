def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    num_of_digits = len(digits)
    armstrong_digits = [d**num_of_digits for d in digits]
    return sum(armstrong_digits) == n
