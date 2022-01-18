# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class form:
    def __init__(self, name, age, phonenumber, email):
        self.name=name
        self.age=age
        self.phonenumber=phonenumber
        self.email=email
f1=form("Jonathan",29, "650","jsiu")
f2=form("Jon",18, "415","jons")
print(f1.name)
print(f2.phonenumber)

print(f1)
#how do I print out all of the variables?