# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************


def star_decorator(function):
    def wrapper():
        func=function()
        make_star=f"*****\n{func}\n*****"
        # how to make this a string so that it can be cap
        return make_star
    return wrapper

@star_decorator
def greeting():
    return "Hello!"

greeting()
print(greeting())