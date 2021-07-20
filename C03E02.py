# Movie Problem

name = input("Please Enter Your Name: ")
age = int(input("Please Enter Your Age: "))
upper_name = name.upper()
letter = upper_name[0]
if letter == "A" and age >= 18:
    print("\nYou Can Watch this Movie")
elif letter != "A" and age < 18:
    print("\nSorry You Can't Watch This Movie")
elif letter != "A":
    print("\nSorry, Your Name Not Starting from 'A' You Can't Watch This Movie")
elif age < 18:
    print("\nSorry, You Are Below 18 You Can't Watch This Movie")
