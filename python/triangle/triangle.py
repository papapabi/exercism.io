def is_equilateral(sides):
    return len(set(sides)) == 1 and is_triangle(sides) \
            and not _has_zero_sides(sides)

def is_isosceles(sides):
    return 1 <= len(set(sides)) <= 2 and is_triangle(sides) \
            and not _has_zero_sides(sides)

def is_scalene(sides):
    return len(set(sides)) == 3 and is_triangle(sides) \
            and not _has_zero_sides(sides)

def _has_zero_sides(sides):
    return 0 in sides

def is_triangle(sides):
    a, b, c = sides
    return a + b >= c and b + c >= a and a + c >= b
