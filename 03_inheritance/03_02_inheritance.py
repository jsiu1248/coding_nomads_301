# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?

class movie():
    def __init__(self, year, title):
        self.year=year
        self.title=title
class romcom(movie):
    def comedy(self):
        return f"The movie is named {self.title} and it came out {self.year} and it is funny." # return doesn't print it but print does

class actionmovie(movie):
    #overwrite the init of Movie
    def __init__(self, year, title, pg=13):
        self.year=year
        self.title=title
        self.pg=pg
    def action(self):
        return f"The movie is named {self.title} and it came out {self.year} and it is action filled and it is pg-{self.pg}."

m1=movie(2020, "Mission Possible")
m2=actionmovie(year=2001, title="Kung-Fu Hustle")
print(romcom.comedy(m1))
print(actionmovie.action(m2))




