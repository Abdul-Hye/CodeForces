a=[int(i) for i in input().split()]
i=3
j=2
b=a[0]
c=a[1]
count=0
while True:
  b=b*i
  c=c*j
  count+=1
  if b==c:
    count+=1
    break
  elif b>c:
    break
  
  
  
print(count)