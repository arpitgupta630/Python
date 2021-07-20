user = input(
    "Please Enter Alphabets in set of 3 (sperate object by Space): ").split(" ")
print(f"\nThis is Your List: {user}")

# Reversing object


def reverse_obj(ls):
    reverse = []
    for i in ls:
        reverse.append(i[::-1])
    return reverse


print(f"\nReversed Alphabets List: {reverse_obj(user)}")


def reverse_ls(l):
    return l[::-1]


print(f"\nReverse of Your List: {reverse_ls(reverse_obj(user))}")
