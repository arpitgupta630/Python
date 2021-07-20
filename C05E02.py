a = int(input("\nPlease Enter Starting Number For Your List: "))
b = int(input("Please Enter Ending Number For Your List: "))
num = list (range(a,b+1))
print(f"\nThis is Your List: {num}")

# Reverse function
def r_ls(l):
    return l[::-1]
print(f"\nReverse of your List: {r_ls(num)}")

# pop append method

def reverse_ls(ls):
    reverse = []
    for i in range (len(ls)):
        pop_item = ls.pop()
        reverse.append(pop_item)
    return reverse
print(f"\nReverse of Your List: {reverse_ls(num)}")
