# Class Method

class Person:
    instance_counter = 0
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.instance_counter += 1
            
    # We define Class Method From Decorators
    @classmethod
    def count_instance(cls):        # We write cls according to conventions
        return f"You have created {cls.instance_counter} Instances of {cls.__name__} Class"
        
    # This is Instance Method
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
p1 = Person("Arpit", "Gupta", 24)
p2 = Person("Nitin", "Data", 12)
p3 = Person("Anshu", "Data", 1)

print(Person.count_instance())

# Class Method as a Constructor
class Person1:
    instance_counter = 0
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @classmethod
    def from_string(cls, string):
        first,last,age = string.split(',')
        return cls(first, last, int(age))
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
human = Person1.from_string("Arpit,Gupta,24")
print(human.full_name())

# Static Method: It has no connection to class or Instance.
class Person2:
    instance_counter = 0
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    @staticmethod
    def hello():
        return "\nHello I am Static Method  I have some logical connection to Your Class"
    
    @classmethod
    def from_string(cls, string):
        first,last,age = string.split(',')
        return cls(first, last, int(age))
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
print(Person2.hello())