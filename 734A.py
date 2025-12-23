n=int(input())
x=input()
c=0
d=0
for i in x:
  if i=='A':
    c+=1
  else:
    d+=1
if c>d:
  print('Anton')
elif c<d:
  print('Danik')
else:
  print('Friendship')