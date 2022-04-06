# Printing Name Length With and Without Spaces
# Taking User Input Character And Count That Character in Name

name = input("Please Enter Your Name: ")
char = input("Enter a Single Letter of Your Name: ")
# To Remove Left & Right Spaces
upper_name = (name.upper()).strip()
no_space_name = upper_name.replace(
    " ", "")             # To Remove Middle Space
upper_char = char.upper()
print(f"\nYour Name Contain {len(upper_name)} Letters With Spaces")
print(f"Your Name Contain {len(no_space_name)} Letters Without Spaces")
print(
    f"\nLetter You Entered Was Repeated {upper_name.count(upper_char)} Times in Your Name")
