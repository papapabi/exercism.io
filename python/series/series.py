def slices(xs, n):
    """Returns a list of consecutive n elements from xs."""
    if n > len(xs) or n < 1:
        raise ValueError("n must be in [1, len(xs)]")
    return [xs[i:i+n] for i in range(len(xs) - n + 1)]
