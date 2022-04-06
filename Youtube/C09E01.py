user_ls = (input("Please Enter Alphabets in set of 2 (Space Seprated): ")).split()
print(f"\nYour Alphabet List: \n{user_ls}")

# Reverse all string in one line:
re_str = [i[::-1] for i in user_ls]
print(f"\nReverse of Single Set in List: \n{re_str}")

# Reverse whole list in one line:
re_list = re_str[::-1]
print(f"\nReverse of Your Whole list: \n{re_list}")
