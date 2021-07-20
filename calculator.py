user_ls = (input("Enter numbers (space seprated): ")).split()
num_ls = []
for i in user_ls:
    num_ls.append(int(i))

def add(*args):
    temp_add = 0
    for i in args:
        temp_add = temp_add + i
    return temp_add

def sub(*args):
    temp_sub = 0
    for i in args:
        temp_sub = temp_sub - i
    return temp_sub

def multiply(*args):
    temp_multiply = 1
    for i in args:
        temp_multiply *= i
    return temp_multiply

def divide(*args):
    for i in args:
        if i == 0:
            return "Invalid Input Can not divide by or with 0"
    for i in range (1):
        temp_divide = args[0]/args[1]
        break
    if len(num_ls) > 2:
        for i in range(2,len(num_ls)):
            temp_divide = temp_divide/args[i]
        return temp_divide
    else:
        return temp_divide

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

select = int(input("Select operations form 1, 2, 3, 4: "))
  
if select == 1:
    print(add(*num_ls))
  
elif select == 2:
    print(sub(*num_ls))
  
elif select == 3:
    print(multiply(*num_ls))
  
elif select == 4:
    print(divide(*num_ls))
else:
    print("Invalid input")
    