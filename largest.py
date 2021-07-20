ls1 = [1,2,3,4,5]
ls2 = [5,4,32,2,1]

def largest(l):
  num = 0
  for i in range (len(l)):
    if i == 0:
      num += l[i]
    elif l[i]> num:
      num = num*0
      num += l[i]
  return num

print(largest(ls1))
print(largest(ls2))
