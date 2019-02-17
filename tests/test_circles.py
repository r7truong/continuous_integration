'''
A script for unit testing circle.py
'''
import unittest
import math
from scripts import circles


class TestCircleArea(unittest.TestCase):
    '''
    A class that contains a unit test for the functions in circles.py
    '''
    def test_area(self):
        '''
        Tests area when radius >= 0
        '''
        self.assertAlmostEqual(circles.circle_area(1), math.pi)
        self.assertAlmostEqual(circles.circle_area(0), 0)
        self.assertAlmostEqual(circles.circle_area(5.2), math.pi * 5.2**2)

    def test_values(self):
        '''
        Make sure value errors are raised when necessary
        '''
        self.assertRaises(ValueError, circles.circle_area, -2)

    def test_types(self):
        '''
        Make type errors are raised when necessary
        '''
        self.assertRaises(TypeError, circles.circle_area, True)
        self.assertRaises(TypeError, circles.circle_area, "radius")
        self.assertRaises(TypeError, circles.circle_area, 5+3j)
