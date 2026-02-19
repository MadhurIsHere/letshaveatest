import unittest
from calculator import add_numbers

class TestCalculator(unittest.TestCase):
    def test_add(self):
        # This test will crash because 5 - 5 is 0, not 10!
        self.assertEqual(add_numbers(5, 5), 10)

if __name__ == '__main__':
    unittest.main()
