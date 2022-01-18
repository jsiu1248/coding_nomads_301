# Write a unittest test suite in `test_mymath.py`
# for the `subtract_divide()` function shown below.
# Check for more instructions in `test_mymath.py`

def subtract_divide(dividend, x, y):
    try:
        z = x - y
        return dividend / z
    except ZeroDivisionError:
        #return f"This won't work because {x} - {y} = 0."
        print(f"This won't work because {x} - {y} = 0.")
        raise # this should raise the exception on the other check instead

