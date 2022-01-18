# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.
import math
class rectangle():
    def __init__(self,  width, length):
        self.width=width
        self.length=length
    def area(self):
        return self.width*self.length
    def perimeter(self):
        return 2*self.width+2*self.length
class circle():
    def __init__(self, radius):
        self.radius=radius
    def circumference(self):
        return 2*self.radius*math.pi
    def area(self):
        return math.pi*self.radius**2
r1=rectangle(7,5)
c1=circle(4)
print(r1.perimeter())
print(c1.circumference())
print(r1.area())
print(c1.area())

#print(c1.circumference())

# why do I have to return it instead of calling it a variable?