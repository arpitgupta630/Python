def power(x):
    def number(n):
        return n**x
    return number

for_square = power(2)
print(for_square(5))

for_cube = power(3)
print(for_cube(5))
