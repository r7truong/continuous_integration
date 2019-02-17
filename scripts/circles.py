'''
A dummy script to test CI
'''
import math


def circle_area(radius):
    '''
    Returns the area of a circle given its radius

    circle_area: Float -> Float
    '''
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    if type(radius) not in [int, float]:  # pylint: disable=C0123
        raise TypeError("The radius must be a non-negative real number.")
    return math.pi * (radius ** 2)
