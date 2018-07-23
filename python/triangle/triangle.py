def has_no_zero_sides(sides):
    return 0 not in sides

def is_triangle(sides):
    a, b, c = sides
    return a + b >= c and b + c >= a and a + c >= b

def valid_triangle(f):
    def inner(sides):
        return f(sides) and is_triangle(sides) and has_no_zero_sides(sides)
    return inner

@valid_triangle
def is_equilateral(sides):
    return len(set(sides)) == 1 

@valid_triangle
def is_isosceles(sides):
    return 1 <= len(set(sides)) <= 2

@valid_triangle
def is_scalene(sides):
    return len(set(sides)) == 3 
