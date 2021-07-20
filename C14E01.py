from functools import wraps
import time

def calculate_time(funcn):
    @wraps(funcn)
    def wrapper(*args, **kwargs):
        print(f"You are Executing {funcn.__name__} function")
        t1 = time.time()
        returned_value = funcn(*args, **kwargs)
        t2 = time.time()
        print(f"\nThis function executed in {t2-t1} seconds\n")
        return returned_value
    return wrapper

@calculate_time
def square(n):
    return [i**2 for i in range(1,n+1)]

square(1000)