# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

#pseudo code write a few functions
# write tests for them

import unittest

#function for turning column names into lower_case and underscores for non_alphabet
# function for checking cases whens

class test_clean(unittest.TestCase):
    def test_clean_is_not_same(self):
        self.assertIsNot(original, s_1_clean) #see that we changed the column at least know that there is a change
    #def test_clean_int(self):
    def test_values(self):
        self.assertNotIn(0, s_1_clean) #testing 0 not in s_1_clean

if __name__ == '__main__':
    unittest.main()
