# Instance Method: Functions that defines in a class are known as Methods

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    # Define function in Class
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

p1 = Person("Arpit", "Gupta", 24)
print(p1.full_name())

# or

p2 = Person("Bella", "Ciao", 5)
print(Person.full_name(p2))