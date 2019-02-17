import unittest
from scripts import returning


class TestReturn(unittest.TestCase):
    def test_return_1(self):
        result = returning.return_1()
        expect = 1
        self.assertEqual(result, expect)
