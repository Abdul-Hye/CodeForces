n=input()
c1=0
c2=0
for i in n:
  if 65<=ord(i)<=90:
    c1+=1
  else:
    c2+=1
if c1>c2:
  print(n.upper())
else:
  print(n.lower())