ls = [
    1, 2, 3,
    [1, 2, 3],
    "Apple", "556",
    ["Arpit", 23, "Male"],
    4.98, 8.90,
    [9.00, "Banana"]
]

# List counting funcn


def count_ls(l):
    var = 0
    for i in l:
        if type(i) == list:
            var += 1
    return var


print(count_ls(ls))
