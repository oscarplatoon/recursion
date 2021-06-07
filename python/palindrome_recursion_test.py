from palindrome_recursion import palindrome_recursive
from palindrome_recursion import reverse_string
import unittest

class PalindromeRecursionTest(unittest.TestCase):
    
    testPalindromes = ['racecar', 'Noon', 'ciVic', 434, "Sore was I ere I saw Eros.", "A man, a plan, a canal -- Panama"]
    testNotPalindromes = ["nice", 123]

    def test_palindromes(self):
        for str in self.testPalindromes:
            self.assertEqual(palindrome_recursive(str), True)

    def test_not_palindromes(self):
        for str in self.testNotPalindromes:
            self.assertEqual(palindrome_recursive(str), False)

if __name__ == "__main__":
    unittest.main()