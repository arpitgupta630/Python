# Sum till user input
print("\n****FOR LOOP****")
print("\nEXAMPLE NUMBER 1:")
num = int(input("Please Enter a Number: "))
n = 0
for j in range(num+1):
    n += j
print(f"Total from 1 to {num} = {n}")

# User input digit sum
print("\nEXAMPLE NUMBER 2:")
num1 = input("Please Enter a Number with Several Digits: ")
var = 0
for i in range(len(num1)):
    var += int(num1[i])
print(f"Total of Your {len(num1)} digit = {var}")

# Count letters from user name and not repeating by for loop
print("\nEXAMPLE NUMBER 3:")
name = input("Please Enter Your Name: ")
char = ""
upper_name = name.upper()
for k in range(len(upper_name)):
    if upper_name[k] not in char:
        print(f"{upper_name[k]} : {upper_name.count(upper_name[k])}")
        char += upper_name[k]
    k += 1
