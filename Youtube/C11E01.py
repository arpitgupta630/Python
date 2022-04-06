user_num = int(input("Please Enter a Number for power: "))
num1 = int(input("\nPlease Enter Starting Number for Your power List: "))
num2 = int(input("Please Enter Ending Number for Your power List: "))
ls = [i for i in range(num1, num2+1)]
print(f"\nYour List: \n{ls}")


def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "You Didn't Enter any Number"


print(f"\n{user_num} Power of Your List: \n{to_power(user_num,*ls)}")
