OUTER_RADIUS = 10
MIDDLE_RADIUS = 5
INNER_RADIUS = 1
OUT_OF_BOUNDS = 0

def score(x, y):
    """
    Returns the score of the thrown dart landing at coordinate (x, y).
    """
    intermediate = x**2 + y**2
    if intermediate > OUTER_RADIUS**2:
        return OUT_OF_BOUNDS
    if intermediate <= INNER_RADIUS**2:
        return 10
    elif intermediate <= MIDDLE_RADIUS**2:
        return 5
    elif intermediate <= OUTER_RADIUS**2:
        return 1
