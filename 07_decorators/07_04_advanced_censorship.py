# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

"""
def censor(function):
    def wrapper():
        func=function()
        word="Shoot"
        masked=f"{word[0]}{'*'*(len(word)-1)}"
        censor_word=f"{func.replace(word,masked)}" 
        return censor_word
    return wrapper


@censor
def word():
    return "I bumped my toe! Shoot!"

word()
print(word())
"""

#pass words to censor

#how to pass a list of words to be censored 

def censor(function):
    def wrapper():
        func=function()
        word=["Shoot","Crabs"]
        for i in range(len(word)):
            masked=f"{word[i][0]}{'*'*(len(word[i])-1)}"
            func=f"{func.replace(word[i],masked)}" 
        return func
    return wrapper


@censor
def sentence():
    return "I bumped my toe! Shoot! Crabs!"

sentence()
print(sentence())