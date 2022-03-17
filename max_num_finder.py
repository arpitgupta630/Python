ls=[1,2,2,2,3,4,2,4,4,2]


e=[[x,ls.count(x)] for x in set(ls)]
print(e, '\n')

# Method 1:
for i in range(0,len(e)):
   if max([i[1] for i in e])==e[i][1]:
       print(e[i][0])

# Method 2:
print('\n', max(ls, key=ls.count))