# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class laptop:
    def __init__(self,name, system):
        self.name=name
        self.system=system
    def __str__(self):
        return f"The {self.name} is a laptop with the {self.system} system."

    def open(self, open):
        self.open=open
        if self.open.lower()=="on":
            return True
        else: 
            return False

    def run(self, run):
        self.run=run
        if self.run.lower()=="on":
            return True
        else: 
            return False



    def close(self, close):
        self.close=close
        if self.close.lower()=="on":
            return True
        else: 
            return False




class animal():
    def __init__(self,name, color, size):
        self.name=name
        self.color=color
        self.size=size
    def __str__(self):
        return f"The {self.name} is {self.color} and it is {self.size}."

    
class game():
    def __init__(self, name, duration, number_of_players):
        self.name=name
        self.duration=duration
        self.number_of_players=number_of_players
    def __str__(self):
        return f"The {self.name} is {self.duration} minutes long and it needs {self.number_of_players} players."



sony=laptop("Sony","Windows")
print(sony.open('on'))
print(sony)

whale=animal("whale","blue","huge")
catan=game("catan",60, 4)

print(whale)
print(catan)