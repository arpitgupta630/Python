def factorial(n):
    if n == 1:
        return 1
    else:
        temp = 1
        for i in range (1,n+1):
            temp = temp*i
        return temp

print(factorial(5))

# Recurssion
def fact_2(num):
    if num == 1:
        return 1
    else:
        temp = num * fact_2(num-1)
        return temp

print(fact_2(5))

