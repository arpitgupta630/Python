import random
welcome = "Welcome To Number Guessing Game"
print(welcome.center(len(welcome)+8, "*"))
num = int(input("\nGuess a Number Between 1 to 100 You have: "))
win_num = random.randint(1, 100)
for i in range(1, 100):
    if num == win_num:
        print(
            f"\nCONGRATULATIONS!!! You Won, You Guess The Right Number in {i} Attempt")
        break
    elif num < 1 or num > 100:
        print("\nWORNG INPUT!!!")
    elif num > win_num:
        print("\nOops, The Number You Guess is Too High.")
    else:
        print("\nOops, The Number You Guess is Too Low.")
    num = int(input(f"Try Again: "))

# while True :
#     if num == win_num:
#         print(f"\nCONGRATULATIONS!!! You Guess The Right Number in {i} Attempt")
#         break
#     elif num < 1 or num > 100:
#         print("\nWORNG INPUT!!!")
#     elif num > win_num :
#         print("\nOops, The Number You Guess is Too High.")
#     else:
#         print("\nOops, The Number You Guess is Too Low.")
#     num= int(input(f"Try Again: "))
#     i+=1
