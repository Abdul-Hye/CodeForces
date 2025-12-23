a=[int(i) for i in input().split()]
x=a[0]
y=a[1]
z=a[2]
sum=0
for i in range (1,z+1):
  b=i*x
  sum+=b
if y>=sum:
  print(0)
else: 
  print(sum-y)