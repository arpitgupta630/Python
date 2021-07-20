# Kwargs (Keyword Arguments)
# Double Star Argument (**Kwargs)

# Kwargs as parameter
def func(**kwargs):
    print("\n", kwargs)
    print(type(kwargs), "\n")
    for k, v in kwargs.items():
        print(f"{k} : {v}")


func(first_name='Arpit', last_name='Gupta')

# Dictionary Unpacking
d = {'name': 'Arpit', 'age': 22, 'gender': 'male'}
func(**d)


# Sequance for functions with all parameters

'''
PADK
1. parameters
2. *args
3. default parameters
4. **kwargs

'''
def func(name, *args, age = 0, **kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)

func("Arpit",1,2,"arpit","gupta",city = "alwar", state = "Rajasthan")