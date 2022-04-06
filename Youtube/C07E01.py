# Cube finder
num = int(input("Please Enter a Number to Find Cube of 1 to Your Number: "))


def cube(a):
    x = {}
    for i in range(1, a+1):
        x[i] = i**3
    return x


print(f"\nYour Cube List from 1 to {num}:\n{cube(num)}")
