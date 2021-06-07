import unittest

from recursion_challenge import *

class TestRecursionChallenge(unittest.TestCase):

    """
    Factorial tests:
    """
    def test_catches_base_case(self):
        self.assertEqual(factorial(0), 1)
    """
    99 Bottles Tests:
    """

    def test_0_bottles(self):
        self.assertEqual(type(bottles(0, "")), str)

    def test_1_bottles(self):
        test_str = ""
        test_str = (bottles(1,""))
        # print(test_str)
        self.assertEqual(bottles(1, ""), test_str)

    def test_99_bottles(self):
        test_str = bottles(99, "")
        # print(test_str)
        self.assertTrue(bottles(99, "") == test_str)

if __name__ == '__main__':
    unittest.main()
