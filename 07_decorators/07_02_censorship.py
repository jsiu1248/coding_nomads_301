# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"


def censor(function):
    def wrapper():
        func=function()
        word="Shoot"
        masked=f"{word[0]}{'*'*(len(word)-1)}"
        censor_word=f"{func.replace(word,masked)}" #take first letter and then star for the rest
        # how to make this a string so that it can be cap
        return censor_word
    return wrapper


@censor
def word():
    return "I bumped my toe! Shoot!"

word()
print(word())

#pass words to censor