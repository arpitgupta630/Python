# Special Magic Method / Dunder Method

class Phone:                   
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model 
        self._price = max(price,0)
        
    def phone_name(self):
        return f"{self.brand} {self.model}"
        
    def __str__(self):                  # for not giving address of class
        return f"Phone Name: {self.brand} {self.model}\nPhone Price: {self._price}"
    
    def __repr__(self):                 # for represent our output as object (optional)
        return f"\nPhone('Nokia', '1100 Classic', 2500)"
    
    def __len__(self):
        return len(self.phone_name())
    
mobile = Phone('Micromax', 'IN 1', 11499)
print(mobile)
print(len(mobile))
print(repr(mobile))             # Provide a demo Object
