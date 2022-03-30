# Class Variable

# 1. Circle Programe
class Circle:
    pi = 3.14           # Class Variable / Class Attribute
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return Circle.pi * self.radius * self.radius      # Using class Variable
    def circumference(self):
        return 2 * Circle.pi * self.radius                # Using Class Variable
    
c = Circle(4)
print(c.area(), '\n', c.circumference(), '\n')

# 2. Laptop Discount Program (in this program we can change variable but we have to use self)
class Laptop:
    discount_precent = 10                       # Class Variable / Class Attribute
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + " " + model
    def discount(self):
        discount = self.price - ((self.discount_precent/100)*self.price)     # Using Self class Variable   
        return f"Price = {self.price} \nDiscount Applied = {self.discount_precent}% \nFinal Price = {discount}"

device1 = Laptop("Dell", "AU114tx Book", 50000)
print(device1.__dict__)                 # Instance Dict
print(device1.laptop_name,'\n',device1.discount(), '\n')

device2 = Laptop("HP", "Pro-Book", 72000)
device2.discount_precent = 15           # Changing Class Variable
print(device2.__dict__)                 # Instance Dict
print(device2.laptop_name,'\n',device2.discount(), '\n')

device3 = Laptop("Apple", "MacBook Pro", 215000)
device3.discount_precent = 25           # Changing Class Variable
print(device3.__dict__)                 # Instance Dict
print(device3.laptop_name,'\n',device3.discount(), '\n')