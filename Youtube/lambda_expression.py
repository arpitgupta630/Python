# lambda expression (anonymous function)

add = lambda a,b : a+b
print(add(5,6))
print(add,"\n")      # assigned as lambda funcn in memory not with 'add'

# lambda expression practice:

# even checker:
is_even = lambda a : a%2==0
print(is_even(6))

# last character:
last_char = lambda s : s[-1]
print(last_char("Arpit"))

# if-else with lambda expression:
func = lambda s : f"{s} is Greater than 3" if len(s)>3 else f"{s} is lesser than 3"
print(func("Gupta"))
