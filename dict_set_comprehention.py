# Dictionary Comprehension:

num1 = int(input("\nPlease Enter Starting Number for Your Dictionary: "))
num2 = int(input("Please Enter Ending Number for Your Dictionary: "))

# Odd Even with help of dictionary comprehension
odd_even = {i: ('Even' if i % 2 == 0 else 'Odd') for i in range(num1, num2+1)}
print(f"\nOdd Even in Your Dictionary: \n{odd_even}")

# Square of Dictionary with help of dictionary comprehension
square = {num: num**2 for num in range(num1, num2+1)}
print(f"\nSquare of Your Dictionary: \n{square}")

# letter count with help of dictionary comprehention
name = ((input("\nPlease Enter Your Name: ")).upper()).strip()
word_count = {char: name.count(char) for char in name}
print(f"\nLetter Count of Your Name: \n{word_count}")

# Set Comprehension

s = {k**2 for k in range(num1, num2+1)}
print(f"\nSquare of Your Set: \n{s}")          # Unorderd Output

# first letter of names
user = input("\nPlease Enter Names Space Seprated: ").split()
names = set(user)
first = {n[0] for n in names}
print(f"First Letter of your Names: \n{first}")  # Unique Output
