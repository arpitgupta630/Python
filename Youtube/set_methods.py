# Methods of Set:

'''We Can't put List or Dictionary in our Set
s = {[1,2,3.4,"Arpit"],{'name' : "Arpit", 'age' : 24 }}     # Error    '''

example = {1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 8}
print(example)        # unorderd unique item

print("\n")

# Duplicate removal from list
ls = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 8]
print(ls)
unique_ls = list(set(ls))
print(unique_ls)

s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(f"\nNew Set 1 to 9: {s}")

# adding items to sets
s.add(10)
print(f"\nAfter Adding 10 in Set: {s}")

# delete from set
# 1. remove() method
s.remove(3)
print(f"\nDelete 3 from Set with help of Remove Method: {s}")
''' s.remove(11)        # it will give error because 11 is not in the set'''
# 2. discard() method
s.discard(4)
print(f"\nDelete 4 from Set with help of Discard Method: {s}")
s.discard(11)       # no error
print(f"\nDelete 11 from Set with help of Discard Method: {s} (No Error)")

# in Keyword
set_for_in = {'a', 'b', 'c'}
print(f"\nSet: {set_for_in}")
user = input("Input item to check in set: ")
if user in set_for_in:
    print("Present")
else:
    print("Not Present")

# looping
for i in set_for_in:
    print(i)        # unorderd collection so unorder printing

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"\nSet 1: {set1}\nSet 2: {set2}")

# Union method (for union we use "|" pipe)
union_set = set1 | set2
print(f"\nUnion of Set 1 | Set 2: {union_set}")

# Intersection method (for intersection we use "&" and)
intsec_set = set1 & set2
print(f"\nIntersection of Set 1 & Set 2: {intsec_set}")
