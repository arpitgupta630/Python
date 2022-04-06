# Objective:
# What is Class?
'''
Class is a Blueprint
We decide what will be our upcoming object in class.
We decide what functionality our object can perform.
We decide what attribute our object will have.
'''
# How to create a Class?
# What is init method (Constructor)?
# What are attributes, instance variables?
'''
Attribute = first_name, last_name, age
Instance Variables = self.first_name, self.last_name, self.age
'''
# How to create our object/instance
'''
Object/ Instance = p1, p2
'''

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.name = first_name + " " + last_name

p1 = Person("Arpit", "Gupta", 22)
p2 = Person("Nitin", "Data", 22)

print(p1, "\n", p1.name)
print("\n")
print(p2, "\n", p2.name)
