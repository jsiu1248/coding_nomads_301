# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.


num_1=input("Pick a number:")
num_2=input("Pick another number:")
#divided=num_1/num_2
try:
    print(int(num_1)/int(num_2))
except TypeError:
    print("You enter a string or non-number")
except ZeroDivisionError:
    print("You are trying to divide by zero!")





