def on_square(n):
    if not 1 <= n <= 64:
        raise ValueError("can't have n <= 0")
    return 2 ** (n - 1)

def total_after(n):
    if not 1 <= n <= 64:
        raise ValueError("can't have n <= 0")
    squares = (on_square(i) for i in range(1, n + 1))
    return sum(squares)
