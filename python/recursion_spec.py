import unittest

from recursion_challenge import *

class TestRecursionChallenge(unittest.TestCase):
    """
    99 Bottles Tests:
    """

    def test_99_bottles(self):
        self.assertEqual(type(bottles(99, 99)), str)


if __name__ == '__main__':
    unittest.main()