# square function for list
a = int(input("\nPlease Enter Starting Number For Your List: "))
b = int(input("Please Enter Ending Number For Your List: "))
num = list(range(a, b+1))
print(f"\nThis is Your List: {num}")

# Square Function


def square_ls(ls):
    square = []
    for i in ls:
        square.append(i**2)
    return square


print(f"\nSquare of Your List: {square_ls(num)}")
