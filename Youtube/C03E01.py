# Number Guessing Game
welcome = "Welcome To Number Guessing Game"
print(welcome.center(len(welcome)+8, "*"))
num = int(input("\nGuess a Number Between 1 to 100: "))
win_num = 78
if num == win_num:
    print("\nCONGRATULATION!!!, You Won You Guess The Right Number")
elif num > 100 or num < 1:
    print("\nWorng Input")
elif num > win_num:
    print("\nOops, The Number You Guess is Too High")
else:
    print("\nOops, The Number You Guess is Too Low")
