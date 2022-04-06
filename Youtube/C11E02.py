def func(ls, **kwargs):
    if kwargs.get("reverse_str") == "YES":
        return [name[::-1].title() for name in ls]
    else:
        return [name.title() for name in ls]


names = input("Please Enter Names (Space Seprated): ").split()
reverse = (input("Do you want to Reverse Your Name (Yes/No): ")).upper()
print(f"\nYour Name List:\n{func(names, reverse_str = reverse)}")
