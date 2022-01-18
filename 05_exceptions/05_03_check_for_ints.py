# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

i=-1
while i<0:
    integer=input("Please enter an integer")
    try:
        print(int(integer))
        i=1
    except ValueError:
        print("You entered a non-integer")
        i=i-1
