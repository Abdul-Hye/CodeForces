n=int(input())
i=1
while True:
  s=''
  x=n+i
  i+=1
  z=str(x)
  for j in z:
    if j not in s:
      s+=j
  if len(s)==len(z):
    print(x)
    break