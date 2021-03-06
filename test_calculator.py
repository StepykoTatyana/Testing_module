# this code is in the beginning of the test_calculator.py file

import unittest
import calculator

class TestCalculator(unittest.TestCase):  # a test case for the calculator.py module

    def test_add(self):
        # tests for the add() function
        self.assertEqual(calculator.add(6, 4), 10, 'Error when adding two positive numbers')
        self.assertEqual(calculator.add(6, -4), 2)
        self.assertEqual(calculator.add(-6, 4), -2)
        self.assertEqual(calculator.add(-6, -4), -10)


    def test_divide(self):
        # tests for the divide() function
        # ...
        self.assertEqual(calculator.divide(10, 0), 0)
        self.assertRaises(ValueError, calculator.divide, 5, 0)
        with self.assertRaises(ValueError):
            calculator.divide(5, 0)

if __name__ == "__main__":
    unittest.main()