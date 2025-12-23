a=[ int(i) for i in input().split() ]
if a[0]%2==0:
  n=a[0]//2
else:
  n=a[0]//2 +1
x=a[1]
if n<x:
 print((x-n)*2)
else:
  print(x+(x-1))