a=input().split('+')
b=[]
for i in range(len(a)):
  b.append(int(a[i]))

c=[]
for i in range(len(b)-1):
  for j in range(len(b)-1):
    if b[j]>b[j+1]:
      b[j],b[j+1]=b[j+1],b[j]

for i in range(len(b)):
    if i==len(b)-1:
        print(str(b[(i)]),end='')
    else:
        print(str(b[(i)]), end='+')


