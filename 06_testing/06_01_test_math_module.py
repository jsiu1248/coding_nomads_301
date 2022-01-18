# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.
import unittest

import math

class TestYourPackageName(unittest.TestCase):

    def test_equality(self):
        """seeing if the numbers match"""
        self.assertEqual(2*math.pi,3/math.e,"They don't equal")

    def test_raises_error(self):
        """seeing if there is a error"""
        self.assertRaises(ZeroDivisionError, 1/0) # I guess the type errors were working before, but it wasn't printing the error


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")

"""
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
    """