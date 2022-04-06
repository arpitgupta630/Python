def leap_year(num):
    if num % 4 == 0:
        if num % 100 == 0:
            if num % 400 == 0:
                return f"{num} is a Leap Year"
            else:
                return f"{num} is not a Leap Year"
        else:
            return f"{num} is a Leap Year"
    else:
        return f"{num} is not a Leap Year"

year = int(input("Enter year: "))
print(leap_year(year))
