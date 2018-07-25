def on_square(n):
    return __calculate(n)

def total_after(n):
    return __calculate(n) * 2 - 1

def __calculate(n):
    if n > 64 or n < 1:
        raise ValueError("n must be in interval [0, 64]")
    return 1 << (n - 1)
