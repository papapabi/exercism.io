def collatz_steps(n):
    if n <= 0:
        raise ValueError("arg must be greater than 0: collatz_steps({n})")
    return __collatz_recursive(n)

def __collatz_recursive(n, step=0):
    if n == 1:
        return step
    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n + 1
    return __collatz_recursive(n, step+1)
