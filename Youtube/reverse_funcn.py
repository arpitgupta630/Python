ls = [1,2,3,4,5,6]

def rev(l):
    for i in range(0,len(l)-1):
        for j in range(len(l)-1,0,-1):
            if i <= j:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
                i+=1
        break

    return l

print(rev(ls))

name = "tiprA"
temp = ""
for i in range (len(name)-1,-1,-1):
    temp += name[i]
print(temp)