'''
*args is basically a * operator
it helps us to make flexible functions no input boundations
'''


def total(a, b):
    return a + b


print(total(3, 4))       # in this case we can input only two value

# What if we want to input more values


def all_sum(*args):
    return sum(args)


print(all_sum(1, 2, 3, 4))

print("\n")


# normal parameter with *args

def multiply(num1, num2, *args):       # first 2 input will parameters and other will be *args
    multiply = 1
    print(num1, num2)
    print(args)
    for i in args:
        multiply *= i
    return multiply * (num1*num2)


print(multiply(2, 3, 4, 5, 6))

print("\n")


# args as argument

def multiply2(*args):
    multiply2 = 1
    print(args)
    for i in args:
        multiply2 *= i
    return multiply2


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(multiply2(*nums))             # operator * will unpack your list or tuple whatever you input
