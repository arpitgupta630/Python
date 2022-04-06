# Decorator - enhance the functionality of other functions
# @ use for decorators (Syntactic Sugar)

def decorator_funcn(any_funcn):
    def wrapper_funcn():
        print ("this is awesome function")
        any_funcn()
    return wrapper_funcn

@decorator_funcn    # Shortcut
def funcn():
    print("this is funcn\n")

funcn()

# funcn with argument

def decorator_funcn2(any_funcn):
    def wrapper_funcn(*args,**kwargs):
        print ("this is awesome function")
        any_funcn(*args,**kwargs)
    return wrapper_funcn

@decorator_funcn2    # Shortcut
def funcn1(a):
    print(f"this is funcn is with argument {a}\n")

funcn1(5)

# function is returning anything

def decorator_funcn3(any_funcn):
    def wrapper_funcn(*args,**kwargs):
        '''This is wrapper function'''
        print ("this is awesome function")
        return any_funcn(*args,**kwargs)
    return wrapper_funcn

@decorator_funcn3    # Shortcut
def funcn2(*args):
    '''This is my define Sum Function'''
    return sum(args)

print(funcn2(5,10,15,20))
print(funcn2.__doc__) 
print(funcn2.__name__) 

print("\n")

# doc string

from functools import wraps
def decorator_funcn4(any_funcn):
    @wraps(any_funcn)
    def wrapper_funcn(*args,**kwargs):
        print ("this is awesome function")
        return any_funcn(*args,**kwargs)
    return wrapper_funcn

@decorator_funcn4    # Shortcut
def funcn3(*args):
    '''This is my define Sum Function'''
    return sum(args)

print(funcn3(5,10,15,20,50))
print(funcn3.__doc__)           # before importing modules doc string shown of wrapper_funcn 
print(funcn3.__name__)          # before importing modules name shown of wrapper_funcn

print("\n")

# <----------practice 1 ----------->

def print_funcn_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        '''This is wrapper function'''
        print(f"You are calling {function.__name__} function")
        print(function.__doc__)
        return function(*args,**kwargs)
    return wrapper

@print_funcn_data
def multiply(*args):
    '''This Function Multiply numbers that you gave in input'''
    temp = 1
    for i in args:
        temp *= i
    return temp

print(multiply(2,3,4,5))

print("\n")

# <-------- practice 2 -------->

def only_int_allow(funcn):
    @wraps(funcn)
    def wrapper(*args, **kwargs):
        check_ls = [(type(i)==int or type(i)==float) for i in args]
        if all(check_ls):
            return funcn(*args,**kwargs)
        else:
            return ("Wrong Input!!!")   
    return wrapper         

@only_int_allow
def my_add(*args):
    return sum(args)

print(my_add(1,2.5,3.5,4,"arpit"))

print("\n")

# <---------- practice 3 ----------> (decorators with argument)

def only_allow(data_type):
    def decorator(funcn):
        @wraps(funcn)
        def wrapper(*args, **kwargs):
            check_ls = [type(i)==data_type for i in args]
            if all(check_ls):
                return funcn(*args,**kwargs)
            else:
                return ("Wrong Input!!!")   
        return wrapper
    return decorator

@only_allow(str)
def str_join(*args):
    string = ""
    for i in args:
        string += i
    return string
print(str_join("arpit ", "gupta"), "\n")

@only_allow(int)
def multiply2(*args):
    temp = 1
    for i in args:
        temp *= i
    return temp
print(multiply2(1,2,3,4,5))
