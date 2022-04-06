'''
define genrator function
take one number as argument
genrate a even sequence of even number from 1 to input number

'''

def even_till(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i

for i in even_till(11):
    print (i)