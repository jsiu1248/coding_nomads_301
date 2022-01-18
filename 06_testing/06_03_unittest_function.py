# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)

#create function
#create two tests

# split a list. take length and replace it with randomized numbers

import unittest
import random
class clean:  #another class parent class
    def __init__(self, string_1):
        self.string_1=string_1

    def clean (self):
        length_list=[]
        string_list=self.string_1.split()
        for i in string_list:
            #string_length.append(len(i))
             length_list.append(random.randrange(len(i)))

        return length_list
        

s_1="hello it is a very good thing to meet you today"
s_1_clean=clean(s_1)
print(s_1_clean.clean())


class test_clean(unittest.TestCase):
    def test_clean_is_not_none(self):
        self.assertIsNotNone(s_1_clean)
    #def test_clean_int(self):
    def test_clean(self):
        self.assertIsNone(s_1_clean)

if __name__ == '__main__':
    unittest.main()

# hm. What is the F and . not in order