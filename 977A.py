n=[int(i) for i in input().split()]
x=n[0]
y=n[1]
for i in range(1,y+1):
  if x%10==0:
    x=x//10
  else:
    x=x-1
print(x)