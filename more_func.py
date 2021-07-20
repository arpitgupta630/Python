'''

We Use Enumerate Function with for loop to track index number
of our Item in iterable (like: List, Tuple, String)

'''

names = ['ArSh', 'Arpit', 'Anshu', 'Gupta', 'Nitin', 'Data']
print(f"List: {names}\n")

print("Without Enumerate Function")
# approch without enumerate func:
index = 0
for name in names:
    print(f"On {index} : {name}")
    index += 1

print("\nWith Enumerate Function")
# approch with enumerate func:
for index, name in enumerate(names):
    print(f"On {index} : {name}")

# find index
def index_finder(ls,name):
    for index, i in enumerate(ls):
        if i == name:
            return f"{name} is on: {index} index"
    return f"{name} Not Found!!!"

print(f"\n{index_finder(names,'Dat')}\n")


# map() function [map function is itrator]

square = list(map(lambda a:a**2, list(range(1,11))))
print(square)

# looping in map()

length_map = map(len,names)

for i in length_map:
    print(i)
# this loop will run only one time bcoz map is itrator to run it two time make it itrable(list or tuple)

print("\n")

# filter() funcn:
evens = tuple(filter(lambda a:a%2==0, list(range(1,11))))
print(evens)

# looping in filter()

odds = filter(lambda a:a%2!=0, list(range(1,11)))
for i  in odds:
    print(i)
# this loop will run only one time bcoz filter is itrator to run it two time make it itrable(list or tuple)

print("\n")

# zip() funcn:
user = ["User_1", "User_2", "User_3"]
first_name = ["Arpit", "Rajesh", "Prateek"]

print(list(zip(user,first_name)))
# if a tuple in list contain 2 objects like [(a,1),(b,2)] we can convert them to dictionary
print(dict(zip(user,first_name)))

print("\n")
# we can use zip for more than 2 objects
last_name = ["Gupta", "Chaursiya", "Sapra"]

print(list(zip(user,first_name,last_name)))

print("\n")
ls = [(1,2),(3,4),(5,6),(7,8)]

ls1,ls2 = list(zip(*ls)) # first seprate both list like [(1,3,5,7), (2,4,6,8)] from zip(*ls) then unpacking

ls1 = list(ls1)
ls2 = list(ls2)
print(ls1)
print(ls2)

# for finding greater from both list
new_ls = []
for pair in zip(ls1,ls2):
    new_ls.append(max(pair))
print(new_ls)

print("\n")

# any & all funcn
num1 = [2,4,6,8,10]
num2 = [1,3,5,7,9,10]

print(any([i%2==0 for i in num1]))
print(any([i%2==0 for i in num2]))
print("\n")
print(all([i%2==0 for i in num1]))
print(all([i%2==0 for i in num2]))

print("\n")

# Closure (function returning function/ first class function)

def power(x):
    def number(n):
        return n**x
    return number

for_square = power(2)
print(for_square(5))

for_cube = power(3)
print(for_cube(5))