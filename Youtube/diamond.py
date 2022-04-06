# Left side of diamond
for i in range (11):
    print(' '*(11-i),'*'*i )
for i in range (11):
    print( " "*i,'*'*(11-i), )

# right side of diamond
for i in range (11):
    print("\t\t",'*'*i )
for i in range (11):
    print("\t\t",'*'*(11-i), )

# combining of diamond
for i in range (11):
    print(' '*(11-i),'*'*i,'*'*i)
for i in range (11):
    print(" "*i,'*'*(11-i),'*'*(11-i))

