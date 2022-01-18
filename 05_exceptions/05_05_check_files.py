# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

from os import execlp


file_name = 'C:\\Users\\jsiu\\Documents\\codingnomads\\python-301-main_jsiu\\python-301-main\\05_exceptions\\integers.txt'
import math

file=open(file_name, "r")
num_1=file.readline()

num_2=input("Pick a number: ")

try: 
    print(num_1/num_2)
except TypeError:
    print("non-number")
except ZeroDivisionError:
    print("You are trying to divide by zero")
