import math

def circle_area(radius):
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    if type(radius) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    return math.pi * (radius ** 2)