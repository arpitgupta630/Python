# user input for number list
num1 = int(input("\nPlease Enter Starting number for your List: "))
num2 = int(input("Please Enter Ending number for your List: "))
num_list = [i for i in range(num1, num2+1)]
print(f"Your Number List: \n{num_list}")

# Creating Square list in line:
sq_list = [i**2 for i in range(num1, num2+1)]
print(f"\nYour Square List: \n{sq_list}")

# Creating Negative list in one line:
neg_list = [-j for j in range(num1, num2+1)]
print(f"\nYour Negative List: \n{neg_list}")

# if statement in list comprehension: for odd even list in 3 line
even_num = [x for x in num_list if x % 2 == 0]
odd_num = [y for y in num_list if y % 2 != 0]
all_num = [even_num, odd_num]
print(f"\nEven & Odd Number in Your List: \n{all_num}")

# if-else statement in list comprehension for odd become negative value and even become square
odd_even = [a**2 if a % 2 == 0 else -a for a in num_list]
print(f"\nOdd will negative and even will square: \n{odd_even} ")

# user input for name list
cycle = int(input("\nHow Many Names do You Want to add: "))
names = []
for i in range(cycle):
    str_list = input("Please Enter Name: ")
    names.append(str_list)
print(f"Your Name List: \n{names}")

# Creating first letter of names list in one line:
name = [i[0] for i in (names)]
print(f"\nList of First Letters of Your Names: \n{name}")

# genrating nested list with help of list comprehention
num3 = int(input("\nPlease Enter Starting number for your Nested List: "))
num4 = int(input("Please Enter Ending number for your Nested List: "))
num5 = int(input("How Many Sub-List You want to Create: "))
ls = [[i for i in range(num3, num4+1)] for j in range(num5)]
print(f"\nNested List:\n{ls}")
