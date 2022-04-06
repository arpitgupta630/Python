# Exception handling by try, expect, else, finally clauses:

# Introduction to Custom Exceptions
class NegativeError(ValueError):
    pass

while True:
    try:
        age = int(input("Enter Your Age: "))
        if age <= 0:
            raise NegativeError
    
    except NegativeError:
        print('\nAge can not be in Negative Form\n')
        
    except ValueError:
        print('\nERROR! You have Entered String instead of Integer, Try Again\n')
    
    else:                               # This will run when there is no error
        if age < 18:
            print("\nYou are below age limit You can not Play this Game")
        else:
            print("\nYou Can Play this Game")
        break
    finally:                            # This will always run no matter if there is error or not
        print('\nFinally Block Runs.......\n')
