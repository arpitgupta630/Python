def prime_number(num):
    prime_ls = [1]
    for number in range(1,1000):
        for divider in range (2,number):
            if (number % divider) == 0:
                break
        else: 
            prime_ls.append(number)
    
    if num <= 0:
        return "\nINVALID INPUT!!! Zero or Negative Input are Not allowed"
    elif num in prime_ls:
        return f"\n{num} is a Prime Number"
    else:
        for divid in range (2,num):
            if (num % divid) == 0:
                return f"\n{num} is Not Prime \nBecause: {divid} x {num//divid} = {num}"
                break
        
user_num = input("\nEnter a Number for Prime Number Calculation: ")
try:
    user_num = int(user_num)

except ValueError:
    print("\nDecimal Value are Not Allowed")

else:
    user_num = int(user_num)
    print(prime_number(user_num))
