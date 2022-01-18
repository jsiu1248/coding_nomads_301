# Create another child class that inherits from `Ingredient()`. You can use
# the code you wrote yourself, or continue working with the one provided below.
# Implement at least one extra method for your child class, and override the
# `expire()` method from the parent `Ingredient()` class.

class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        if self.name=="salt":
            print(f"{self.name} never expires")
        else:
            """Expires the ingredient item."""
            print(f"whoops, these {self.name} went bad...")
            self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

class Meat(Ingredient):
    """A meat for your food."""
    def store(self):
        print(f"You have {self.amount} of stored {self.name} meat in the fridge")
    def expire(self):
        print(f"{self.name} expires in three days")

c = Ingredient("salt", 3)
p = Spice("pepper", 20)
b=Meat("beef","16 ounces")
c.expire()
p.expire()
b.expire() # polymorphism in Python. Both classes have a method with the same name, but the methods have different effects.