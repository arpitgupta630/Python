ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(ls[2], "\n")                # It will print sublist on 2 index

# For Loop To print all numbers
for sublist in ls:
    for i in sublist:
        print(i, end=" ")

print("\n")

# For printing single number from list
print(ls[1][-1])
print(ls[-1][0])
print(ls[-2][-3])
