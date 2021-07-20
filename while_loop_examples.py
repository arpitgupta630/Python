print("\n****WHILE LOOP EXAMPLES****")

# User input number sum while loop
print("\nEXAMPLE NUMBER 1:")
num = int(input("Please Enter a Number: "))
total = 0
i = 0
while i <= num:
    total += i
    i += 1
print(f"Total From 1 to {num} = {total}")

# User input Digit Total
print("\nEXAMPLE NUMBER 2:")
num1 = input("Please Enter a Number With Several Digit: ")
t = 0
j = 0
while j < len(num1):
    t += int(num1[j])
    j += 1
print(f"Sum of Your {len(num1)} digit = {t}")

# Letter count of user input name without repeating letter with while loop
print("\nEXAMPLE NUMBER 3:")
name = input("Please Enter Your Name: ")
upper_name = name.upper()
char = ""
k = 0
while k < len(upper_name):
    if upper_name[k] not in char:
        print(f"{upper_name[k]} : {upper_name.count(upper_name[k])}")
        char += upper_name[k]
    k += 1
