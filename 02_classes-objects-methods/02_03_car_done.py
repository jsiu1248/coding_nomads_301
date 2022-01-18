# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class car():
    def __init__(self, model, year, max_speed):
        self.model=model
        self.year=year
        self.max_speed=max_speed
    def increase_speed(self):
        self.max_speed=self.max_speed+5
        #what happens when I don't have self. on the left side?
        #how do I make it keep on increasing?
    def details(self):
        print(f"model:{self.model} year:{self.year} max_speed:{self.max_speed}")

tesla=car("x",2019,150)
toyota=car("crv",2018,120)

toyota.increase_speed()
toyota.details()
tesla.details()