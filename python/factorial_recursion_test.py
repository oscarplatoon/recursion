import unittest
from factorial_recursion import factorial

class RecursiveFactorialTest(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(factorial(0), 1)
    
    def test_one_input(self):
        self.assertEqual(factorial(1), 1)

    def test_input1(self):
        self.assertEqual(factorial(5), 120)

    def test_input2(self):
        self.assertEqual(factorial(45), 119622220865480194561963161495657715064383733760000000000 )
    
    def test_input3(self):
        self.assertEqual(factorial(99), 933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208272237582511852109168640000000000000000000000)

if __name__ == '__main__':
    unittest.main()