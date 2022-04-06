a = int(input("Please Enter Starting Number for Your List: "))
b = int(input("Please Enter Ending Number for Your List: "))
num = list(range(a, b+1))
print(f"\nThis is Your List: {num}")

# filter odd and even number in one list


def odd_even(ls):
    odd = []
    even = []
    for i in ls:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [odd, even]


print(f"\nOdd & Even Number in Your List: {odd_even(num)}")
