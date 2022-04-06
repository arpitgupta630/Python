# Make a Class for applying discount on laptop Price:

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + " " + model
    def discount(self, value):
        discount = self.price - ((value/100)*self.price)
        return f"Price = {self.price} \nDiscount Applied = {value}% \nFinal Price = {discount}"

device1 = Laptop("HP", "Pro-Book", 72000)
print(device1.laptop_name,'\n',device1.discount(20))

print('\n')

device2 = Laptop("Dell", "DRX1101", 60000)
print(device2.laptop_name,'\n',device2.discount(20))