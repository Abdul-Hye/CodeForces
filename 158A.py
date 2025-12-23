a=input().split()
b=[int(i) for i in a]
c=input().split()
d=[int (j) for j in c]
count=0
x=b[1]-1
for i in range(len(d)):
  if d==[0]*(b[1]):
    count=0
  elif d[i]!=0 and d[i]>=d[x]:
    count+=1
 
print(count)
