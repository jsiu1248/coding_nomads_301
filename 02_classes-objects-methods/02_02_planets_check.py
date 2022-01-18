# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self,name, color, system):
        self.name=name
        self.color=color
        self.system=system
    
    def __str__(self):
        return f"Planet {self.name} is a {self.color} plant in the {self.system}"
    
    def bears_life(self):
        if self.color.lower()=="blue":
            return True
        else:
            return False

mars=Planet("Mars", "red","Solar System")
earth=Planet("Earth","blue","Solar System")

print(mars.name, mars.color, mars.system)

#why does it say typererror and takes no arguments? # I guess I didn't put the last __ but it was weird that it still worked

print(mars) # without calling the __str__ method then it would just return the object location
print(earth.bears_life())