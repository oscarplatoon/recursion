from recursion_challenge import factorial, palindrome, bottles
import unittest


class FactorialTest(unittest.TestCase):

  def test_correct_response(self):
    self.assertEqual(factorial(1), 1)
    self.assertEqual(factorial(5), 120)


class PalindromeTest(unittest.TestCase):

  def test_correct_response(self):
    self.assertEqual(palindrome('racecar'), 'This is a palindrome')
    self.assertEqual(palindrome('poop'), 'This is a palindrome')

  def test_not_palindrome(self):
    self.assertEqual(palindrome('teststring'), 'This is not a palindrome')
    self.assertEqual(palindrome('example'), 'This is not a palindrome')


class bottles(unittest.TestCase):

  def test_bottles(self):
    self.__str__(bottles(1), 'No more bottles')

  def test_multiple(self):
    self.assertEqual(bottles(5), (f'{5} bottles of beer on the wall, {5} bottles of beer.')
		(f'Take one down and pass it around, {4} bottles of beer on the wall.'))

if __name__ == '__main__':
    unittest.main()