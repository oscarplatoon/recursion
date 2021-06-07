from recursion_challenge import factorial, palindrome
import unittest

class FactorialTest(unittest.TestCase):
  def test_correct_response(self):
    self.assertEqual(factorial(1), 1)


class PalindromeTest(unittest.TestCase):

  def test_correct_response(self):
    self.assertEqual(palindrome('racecar'), 'This is a palindrome')

if __name__ == '__main__':
    unittest.main()