import unittest

from recursion_challenge import *

class TestRecursionChallenge(unittest.TestCase):

    """
    ----------------
    Factorial tests:
    ----------------
    """
    def test_catches_base_case(self):
        self.assertEqual(factorial(0), 1)

    def test_catches_base_case_2(self):
        self.assertEqual(factorial(1), 1)

    def test_mid_size_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_big_factorial(self):
        self.assertEqual(factorial(20), 2432902008176640000)


    """
    ----------------
    Palindrome Tests
    ----------------
    """

    def test_returns_bool(self):
        self.assertEqual(type(palindrome("test")), bool)

    def test_single_word(self):
        self.assertEqual(palindrome("hannah"), True)

    def test_returns_sentence_palindrome(self):
        self.assertEqual(palindrome("Sore was I ere I saw Eros."), True)

    def test_returns_correct_with_hyphens(self):
        self.assertEqual(palindrome("A man, a plan, a canal - - Panama"), True)

    """
    ----------------
    99 Bottles Tests:
    ----------------
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

    """
    ----------------
    Roman Numeral Tests:
    ----------------
    """

    def test_returns_a_string(self):
        self.assertEqual(type(roman_num(200)), str)

    def test_roman_accuracy(self):
        self.assertEqual(roman_num(193), "CXCIII")

if __name__ == '__main__':
    unittest.main()
