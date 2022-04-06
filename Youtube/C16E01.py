# Create class name laptop with attribute: brand name, model name, price
# create two object/instance for laptop class

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + " " + model

device1 = Laptop("HP", "Pro-Book", 72000)
device2 = Laptop("Dell", "DRX1101", 60000)

print(device1.laptop_name)
print(device2.laptop_name)