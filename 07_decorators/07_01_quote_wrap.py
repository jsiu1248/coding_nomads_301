# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.




def cap_decorator(function):
    def wrapper():
        func=function()
        make_cap=func.title()
        # how to make this a string so that it can be cap
        return make_cap
    return wrapper

@cap_decorator
def greeting():
    return "Hello world!"

greeting()
print(greeting())