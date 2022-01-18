# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

#three levels

class Vehicle():
    def __init__(self, name, color, type):
        self.name=name
        self.color=color
        self.type=type


class Truck(Vehicle):
    def __init__(self, name, color, type, speed):
        super().__init__(name, color, type)
        self.speed=speed
    def drive(self, speed):

        if self.type=="truck":
            return f"{self.name} is a type of truck and it is {self.color}."

class Motorcycle(Vehicle):
    def __init__(self, name, color, type, speed):
        super().__init__(name, color, type)
        self.speed=speed
    def drive(self, speed):

        if self.type=="motorcycle":
            return f"{self.name} is a type of motorcycle and it is {self.color}."



class Semi(Truck):
    def park(self):
        return f"{self.name} is a type of truck and it is {self.color} and it is going {self.speed}."

class Scooter(Motorcycle):
    def park(self):
        return f"{self.name} is a type of motorcycle and it is {self.color} and it is going {self.speed}."

semi_1=Semi(name="Ford", color="blue", type="truck", speed=10)
scooter_1=Scooter(name="Honda", color="black", type="motorcycle", speed=15)

print(semi_1.park())
print(scooter_1.park())
