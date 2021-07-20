ls = [True, False, 1, 2, 3, 4, 1.235, 6.32, [9, 8, 7, 6.3], 'arpit']


def int_str(l):
    return [str(i) for i in ls if (type(i) == int or type(i) == float)]


print(int_str(ls))
