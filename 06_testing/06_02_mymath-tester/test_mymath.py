# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `ZeroDivisionError` gets raised correctly.

import unittest

from mymath import subtract_divide 

class TestYourPackageName(unittest.TestCase):

    def test_subtract_divide(self):
        """seeing if the numbers work"""
        result=subtract_divide(1,2,3)
        self.assertEqual(result,-1,"They don't equal")

    def test_zero_division_error(self):
        """seeing if there is a error"""
        with self.assertRaises(ZeroDivisionError):
        # I guess the type errors were working before, but it wasn't printing the error
            result_2=subtract_divide(0,2,2)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")

