import unittest
from roman_numerals_recursion import arabic_to_roman

class RomanNumeralsTests(unittest.TestCase):

    def test_case_VI(self):
        self.assertEqual(arabic_to_roman(6), "VI")

    def test_case_IV(self):
        self.assertEqual(arabic_to_roman(4), "IV")
    
    def test_case_DV(self):
        self.assertEqual(arabic_to_roman(505), "DV")
    
    def test_case_CMXLIV(self):
        self.assertEqual(arabic_to_roman(944), "CMXLIV")

    def test_case_DCCXXXIX(self):
        self.assertEqual(arabic_to_roman(739), "DCCXXXIX")

if __name__ == '__main__':
    unittest.main()

