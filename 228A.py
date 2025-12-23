count=0
a=[int (i) for i in input().split()]
b=[]
for i in a:
  if i not in b:
    b.append(i)
print(len(a)-len(b))
