import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(0, 100), 0)

    def test_division(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(-8, 2), -4)
        self.assertEqual(divide(-8, -2), 4)
        with self.assertRaises(ValueError):
            divide(10, 0)

# The below code is needed to run the tests
if __name__ == '__main__':
    unittest.main()
