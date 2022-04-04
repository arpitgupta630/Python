# Raise Error

def addition(a,b):
    if (type(a) is int) and (type(b) is int):
        return a + b
    raise TypeError ('You are passing Worng data type!')

print(addition(2,3))
# print(addition('2','3'))            # This will throw a TypeError  

# NotImplementedError

class Animal:
    def __init__(self, name):
        self.name = name
        
    def sound(self):                            # This is abstract method becoz it is empty
        raise NotImplementedError('Sound Method not defined in Sub-Classes')
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        return f'\nWoof Woof\nMy name is {self.name}\nAnd I am a {self.breed}'
        
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

pet1 = Dog('Tuffy', 'German Shepard')
print(pet1.sound())

pet2 = Cat('Charlie', 'Persian')
# print(pet2.sound())                   # This will throw NotImplementedError

print('\n')

# One more Example

class Mobile:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
class Mobile_store:
    def __init__(self):
        self.mobiles = []
        
    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError(f"\'{new_mobile}\' should be object of Mobile class")

mobile1 = Mobile("Apple iPhone 13 Pro")
shop = Mobile_store()
shop.add_mobile(mobile1)
print(shop.mobiles[0].name)

mobile2 = 'Oneplus 8T'
# shop.add_mobile(mobile2)              # This will throw a type Error           
# print(shop.mobiles[1].name)