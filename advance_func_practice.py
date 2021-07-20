# zip() funcn practice

ls1 = [1,2,3]
ls2 = [4,5,6]
ls3 = [7,8,9]

def average_finder(*args):
    average = []
    for pair in zip(*args):
        avg = sum(pair)/len(pair)
        average.append(avg)
    return average

print(average_finder(ls1,ls2,ls3))

# by lambda funcn (anonymus func)

average_finder_lambda = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder_lambda(ls1,ls2,ls3))

print("\n")

# all() func use/practice ----> to avoid wrong input

def total(*args):
    if all([(type(i) == int or type(i) == float) for i in args]):
        return sum(args)
    else:
        return "Worng Input!!!"

print(total(1,2,3,4,5,10.5, 'arpit'))

print("\n")

# advance max() & min() funcn
name = ["Arpit","Ashish", "Rome", "is",'not','a']
print(max(name, key = lambda i : len(i)))
print(min(name, key = lambda i : len(i)))

print("\n")

# simple data structure
student = [
    {'name': 'Arpit', 'score' : 90, 'age' : 23},
    {'name': 'Ashish', 'score' : 70, 'age' : 27},
    {'name': 'Nitin', 'score' : 50, 'age' : 21}
]
print(max(student, key = lambda i : i.get('score')))
print(max(student, key = lambda i : i.get('score'))['name'])
print('\n')
print(min(student, key = lambda i : i.get('score')))
print(min(student, key = lambda i : i.get('score'))['name'])

print("\n")

# complex data structure
student2 = {
    'Arpit' : {'score' : 90, 'age' : 23},
    'Ashish': {'score' : 70, 'age' : 27},
    'Nitin': {'score' : 50, 'age' : 21}
}
print(max(student2, key = lambda i : student2[i]['score']))

# sorted() funcn

employee_details = [
    {'name': 'arpit', 'position': 'analyst', 'package': 2150000},
    {'name': 'prateek', 'position': 'developer', 'package': 2000000},
    {'name': 'mohit', 'position': 'sales', 'package': 1200000}
]

print(sorted(employee_details,key= lambda i : i.get('package')))