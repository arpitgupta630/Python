class Phone:                   # Parent Class / Super Class / Base Class
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model 
        self._price = max(price,0)      # _price is private according to convantion
    
    def full_name(self):
        return f"\bPhone Name: {self.brand} {self.model}\nPhone Price: {self._price}"
    
class Smartphone(Phone):       # Child Class / Sub Class / Derived Class 
    
    def __init__(self, brand, model, price, ram, storage, rear_camera, front_camera):
        super().__init__(brand, model, price)               # Importing attribute from parent class
        self.ram = ram
        self.storage = storage
        self.rear_camera = rear_camera
        self.front_camera = front_camera
    
    def specification(self):
        return f"Specification:\nRAM and Internal Storage: {self.ram} GB and {self.storage} GB\nFront and Rear Camera: {self.front_camera} MP and {self.rear_camera}\nPhone Price: {self._price}\n"
    
class Flagship(Smartphone):         # Multilevel Inheritance
    
    def __init__(self, brand, model, price, ram, storage, rear_camera, front_camera, processor):
        super().__init__(brand, model, price, ram, storage, rear_camera, front_camera)
        self.processor = processor
        
mobile1 = Phone('Nokia','1100',2500)
print("\nKeypad Phone:\n", mobile1.full_name())

mobile2 = Smartphone('Micromax', 'IN 1', 11499, 8, 128, 48, 8)
print("\nSmartphone:\n", mobile2.full_name())
print(mobile2.specification())

mobile3 = Flagship('Apple', 'iPhone 13 Pro Max', 159900, 12, 512, 64, 16, 'A15 Bionic Chip')
print("\nFlagship Phone:\n", mobile3.full_name())
print(mobile3.specification(), f"\bProcessor: {mobile3.processor}")