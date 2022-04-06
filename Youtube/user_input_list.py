# ls = [1,2,3,[1,2,3],"Apple","556",["Arpit",23,"Male"], 4.98, 8.90,[9.00,"Banana"]]
# Making this type of list with help of user input

main_ls = []

# for Integer Input in Main List
int_confirm = (input("\nDo You Want to add Integer to Your List (Yes/No): ")).upper()
integer = int_confirm.replace(" ", "")
if integer == "YES":                      # Case Insensitive Input
    int_time = int(input("How Many Integer do You Want to add in your List: "))
    for i in range(int_time):
        int_list = int(input("\nPlease Enter Integer: "))
        position_int = int(
            input("Which Place Do You want to add Your Integer in List: "))
        main_ls.insert(position_int-1, int_list)

# print(f"\nYour List With Integer (if u agreed): \n{main_ls}")

# for float Input in Main List

float_confirm = (
    input("\nDo You Want to add Float to Your List (Yes/No): ")).upper()
float_value = int_confirm.replace(" ", "")
if float_value == "YES":                      # Case Insensitive Input
    float_time = int(input("How Many Float do You Want to add in your List: "))
    for i in range(float_time):
        float_list = float(input("\nPlease Enter Float: "))
        position_float = int(
            input("Which Place Do You want to add Your Float in List: "))
        main_ls.insert(position_float-1, float_list)

# for String Input in Main List

str_confirm = (
    input("\nDo You Want to Add String to Your List (Yes/No): ")).upper()
user = str_confirm.replace(" ", "")
if user == "YES":                      # Case Insensitive Input
    str_time = int(input("How Many String do You Want to addin Your List: "))
    for i in range(str_time):
        str_list = input("\nPlease Enter Item Names: ")
        position_str = int(
            input("Which Place Do You want to add Your String in List: "))
        main_ls.insert(position_str-1, str_list)

# print(f"\nYour List With Integer and Item (if u agreed): \n{main_ls}")

# for Sub-list Input in Main List

sub_ls_confirm = (
    input("\nDo You Want to Add Sub-list to Your Main List (Yes/No): ")).upper()
user = sub_ls_confirm.replace(" ", "")             # to remove spaces
if user == "YES":                      # Case Insensitive Input
    sub_ls_time = int(input("How Many Sub-list do You Want to add: "))
    x = 0
    for i in range(sub_ls_time):
        x += 1
        sub_ls = []
        sub_ls.clear()
        sub_ls_int = input(f"\nDo You Want to add Integer to your Sub-List no. {x} (Yes/No): ").upper()
        sub_ls_int.replace(" ", "")
        sub_ls_float = input(f"Do You Want to add Float to your Sub-List no. {x} (Yes/No): ").upper()
        sub_ls_float.replace(" ", "")
        sub_ls_str = input(
            f"Do You Want to add String to your Sub-List no. {x} (Yes/No): ").upper()
        sub_ls_str.replace(" ", "")

        if sub_ls_int == sub_ls_float == sub_ls_str == "YES":

            sub_int_time = int(
                input(f"\nHow Many Integer do You Want to add in your Sub-List no. {x}: "))
            for i in range(sub_int_time):
                sub_int_list = int(input("Please Enter Integer: "))
                position_sub_int = int(
                    input("Which Place Do You want to add Your Integer in Sub-List: "))
                sub_ls.insert(position_sub_int-1, sub_int_list)

            sub_float_time = int(
                input(f"\nHow Many Float do You Want to add in your Sub-List no. {x}: "))
            for i in range(sub_float_time):
                sub_float_list = float(input("Please Enter Float: "))
                position_sub_float = int(
                    input("Which Place Do You want to add Your Float in Sub-List: "))
                sub_ls.insert(position_sub_float-1, sub_float_list)

            sub_str_time = int(
                input(f"\nHow Many String do You Want to add in your Sub-List no. {x}: "))
            for i in range(sub_str_time):
                sub_str_list = input("Please Enter String: ")
                position_sub_str = int(
                    input("Which Place Do You want to add Your String in Sub-List: "))
                sub_ls.insert(position_sub_str-1, sub_str_list)

        elif sub_ls_int == sub_ls_float == "YES":

            sub_int_time = int(
                input(f"\nHow Many Integer do You Want to add in your Sub-List no. {x}: "))
            for i in range(sub_int_time):
                sub_int_list = int(input("Please Enter Integer: "))
                position_sub_int = int(
                    input("Which Place Do You want to add Your Integer in Sub-List: "))
                sub_ls.insert(position_sub_int-1, sub_int_list)

            sub_float_time = int(
                input(f"\nHow Many Float do You Want to add in your Sub-List no. {x}: "))
            for i in range(sub_float_time):
                sub_float_list = float(input("Please Enter Float: "))
                position_sub_float = int(
                    input("Which Place Do You want to add Your Float in Sub-List: "))
                sub_ls.insert(position_sub_float-1, sub_float_list)

        elif sub_ls_float == sub_ls_str == "YES":

            sub_float_time = int(
                input(f"\nHow Many Float do You Want to add in your Sub-List no. {x}: "))
            for i in range(sub_float_time):
                sub_float_list = float(input("Please Enter Float: "))
                position_sub_float = int(
                    input("Which Place Do You want to add Your Float in Sub-List: "))
                sub_ls.insert(position_sub_float-1, sub_float_list)

            sub_str_time = int(
                input(f"\nHow Many String do You Want to add in Your Sub-List no. {x}: "))
            for i in range(sub_str_time):
                sub_str_list = input("Please Enter String: ")
                position_sub_str = int(
                    input("Which Place Do You want to add Your String in Sub-List: "))
                sub_ls.insert(position_sub_str-1, sub_str_list)

        elif sub_ls_int == sub_ls_str == "YES":

            sub_int_time = int(
                input(f"\nHow Many Integer do You Want to add in your Sub-List no. {x}: "))
            for i in range(sub_int_time):
                sub_int_list = int(input("Please Enter Integer: "))
                position_sub_int = int(
                    input("Which Place Do You want to add Your Integer in Sub-List: "))
                sub_ls.insert(position_sub_int-1, sub_int_list)

            sub_str_time = int(
                input(f"\nHow Many String do You Want to add to your Sub-List no. {x}: "))
            for i in range(sub_str_time):
                sub_str_list = input("Please Enter String: ")
                position_sub_str = int(
                    input("Which Place Do You want to add Your String in Sub-List: "))
                sub_ls.insert(position_sub_str-1, sub_str_list)

        elif sub_ls_int == "YES":

            sub_int_time = int(
                input(f"\nHow Many Integer do You Want to add in your Sub-List no. {x}: "))
            for i in range(sub_int_time):
                sub_int_list = int(input("Please Enter Integer: "))
                position_sub_int = int(
                    input("Which Place Do You want to add Your Integer in Sub-List: "))
                sub_ls.insert(position_sub_int-1, sub_int_list)

        elif sub_ls_float == "YES":

            sub_float_time = int(
                input(f"\nHow Many Float do You Want to add in your Sub-List no. {x}: "))
            for i in range(sub_float_time):
                sub_float_list = float(input("Please Enter Float: "))
                position_sub_float = int(
                    input("Which Place Do You want to add Your Float in Sub-List: "))
                sub_ls.insert(position_sub_float-1, sub_float_list)

        elif sub_ls_str == "YES":

            sub_str_time = int(
                input(f"\nHow Many String do You Want to add in your Sub-List no. {x}: "))
            for i in range(sub_str_time):
                sub_str_list = input("Please Enter String: ")
                position_sub_str = int(
                    input("Which Place Do You want to add Your String in Sub-list: "))
                sub_ls.insert(position_sub_str-1, sub_str_list)

        position_sub_ls = int(
            input(f"\nWhich Place Do you want to add Your Sub-List no. {x} in Main List: "))
        main_ls.insert(position_sub_ls-1, sub_ls)

print(
    f"\nYour List With Integer, Float, String and Sub-list (if u agreed): \n{main_ls}")
