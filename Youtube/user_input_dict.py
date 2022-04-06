# User input Dictionary

user_info = {}
# for loop range
cycle = int(input("How Many Input you Want to give in Your Dictionary: "))
for i in range(cycle):

    # Key Input
    key_input_type = (input("\nWhich Type of Data You want to Input in Key (Int/str): ")).upper()
    if key_input_type == "INT":
        key_input = int(input("Please Enter Integer Value: "))
    else:
        key_input = input("Please Enter String: ")

    # Confirmation for Integer
    value_t1 = (input("Is your Value Contain Numerical Data (Yes/No): ")).upper()
    value_type1 = value_t1.replace(" ", "")         # Space removal from Confirmatin
    # Conformation for list
    value_t2 = (input("Is your Value Contain More than one Data (Yes/No): ")).upper()
    value_type2 = value_t2.replace(" ", "")

    # If condition for integer in list value input
    if value_type1 == "YES" and value_type2 == "YES":
        value = []
        # int input in list
        int_times = int(
            input("How Many Numerical Value do You want to Enter: "))
        for j in range(int_times):
            value_int = int(input("Please Enter your Numerical Data: "))
            value.append(value_int)
    # If condition for integer value input
    elif value_type1 == "YES":
        value = int(input("Please Enter your Data (Numerical Value only): "))
    # If condition for list value input
    elif value_type2 == "YES":
        value = input("Please Enter your Data (',' Seprated): ").split(",")
    else:
        # str Value Input
        value = input("Please Enter your Data: ")
    user_info[key_input] = value

# printing dictionary
print(f"\nYour Dictionary is Created Succesfully: \n{user_info}\n")

# printing dictionary in colomn
for key, value in user_info.items():
    print(f"{key}\t : {value}")
