n=input()
x=False
a=['4','7']
c=0
for i in n:
  if i in a:
    c+=1
#print(c)
if c==4 or c==7:
  print('YES')
else:
  print('NO')