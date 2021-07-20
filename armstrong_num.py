def armstrong_num(num):
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit**len(str(num))
        temp //= 10

    if num == total:
        return f"{num} is Armstrong Number"
    else:
        return f"{num} is not Armstrong Number"

user_num = int(input("Enter Number to check Armstrong Number: "))
print(armstrong_num(user_num))
