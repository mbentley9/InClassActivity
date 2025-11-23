
import unittest
from main import add, multiply


class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -4), -5)

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(multiply(0, 10), 0)


if __name__ == "__main__":
    unittest.main()
