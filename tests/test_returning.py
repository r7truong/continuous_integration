'''
A script for unit testing returning.py
'''
import unittest
from scripts import returning


class TestReturn(unittest.TestCase):
    '''
    A class that contains a unit test for the function return_1 in returning.py
    '''
    def test_return_1(self):
        '''
        Tests a standard valid case of return_1
        '''
        result = returning.return_1()
        expect = 1
        self.assertEqual(result, expect)
