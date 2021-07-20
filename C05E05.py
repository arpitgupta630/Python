ls1 = input(
    "Please Enter Several Numbers for 1st List (Space Seprated): ").split()
ls2 = input(
    "Please Enter Several Numbers for 2nd List (Space Seprated): ").split()
print(f"\nThis is Your First List: {ls1}")
print(f"This is Your Second List: {ls2}")

# common in both list


def common_ls(a, b):
    common = []
    for i in ls1:
        for j in ls2:
            if i == j:
                common.append(i)
    return common

# or


def c_ls(x, y):
    output = []
    for i in x:
        if i in y:
            output.append(i)
    return output


print(f"\nCommon From Both of Your List: {common_ls(ls1, ls2)}")
print(f"\nCommon From Both of Your List: {c_ls(ls1, ls2)}")
