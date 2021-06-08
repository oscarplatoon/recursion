import unittest

from recursion_challenge import factorial, palindrome, bottles, roman_num

class TestFactorial(unittest.TestCase) :
    def test_anynameyouwant(self) :
        self.assertEqual(factorial(8), 40320)

class TestPalindrome(unittest.TestCase) :

    def test_anynameyouwant(self) :
        self.assertEqual(palindrome(parameter), parameter)

class TestBottles(unittest.TestCase) :

    def test_anynameyouwant(self) :
        self.assertEqual(bottles(5), "No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")

class TestRoman_num(unittest.TestCase) :

    def test_anynameyouwant(self) :
        self.assertEqual(roman_num(parameter), parameter)


if __name__ == '__main__':
    unittest.main()