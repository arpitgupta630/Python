print("\n****FUNCTION PRACTICE****\n")
# Last Character Function
print("Example Number 1:")


def last_char(n):
    return n[-1]


name = input("Please Enter Your Name: ")
print(f"Last Character of your Name is: {last_char(name)}")

# Odd Even Function
print("\nExample Number 2:")


def odd_even(a):
    if a % 2 == 0:
        return "Even Number"
    return "Odd Number"


num = int(input("Please Enter a Number to Check if its Odd or Even: "))
print(f"{num} is {odd_even(num)}")

# Greatest Number
print("\nExample Number 3: ")


def greatest(n1, n2, n3):
    if n1 > n2 > n3:
        return n1
    elif n2 > n1 > n3:
        return n2
    return n3


num1 = int(input("Please Enter First Number: "))
num2 = int(input("Please Enter Second Number: "))
num3 = int(input("Please Enter Third Number: "))
print(f"{greatest(num1,num2,num3)} is Greatest Number Among All Three of Your Input")

# Palindrome function (case insensitive)
print("\nExample Number 4: ")


def is_palindrome(x):
    y = x.upper()
    return y == y[::-1]


user_name = input("Please Enter Your Name: ")
print(f"{user_name} is Palindrome Object: {is_palindrome(user_name)}")
