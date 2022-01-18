# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.


import time




def time_decorator(function):
    def wrapper():
        start_time = time.time()
        start=function()
        str_time=f"--- {time.time() - start_time} seconds ---" 
        return str_time
    return wrapper



@time_decorator
def random_function():
    for i in range(0,100):
        print(i)

print(random_function())

