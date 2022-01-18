# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".


#pass words to censor

#how to pass a list of words to be censored 

def tag_with_html(function):
    def wrapper():
        func=function()
        func=f"<li/>{func}</li>"
        return func
    return wrapper


@tag_with_html
def text_to_tag():
    return "I bumped my toe! Shoot! Crabs!"

text_to_tag()
print(text_to_tag())

#tag with html function
#function for text