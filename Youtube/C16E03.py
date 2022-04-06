# Instance Counter

class Student:
    instance_counter = 0                    # Class Variable / Class Attribute
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade
        Student.instance_counter += 1
    
s1 = Student("Arpit Gupta", 5, 12)
s2 = Student("Kavish Gupta", 21, 11)
# s3 = Student("Rajat Gupta", 45, 10)

print(Student.instance_counter)