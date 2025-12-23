s=input()
t=input()
x=''
for i in range(len(t)-1,-1,-1):
  x+=t[i]
if s==x:
  print('YES')
else:
  print('NO')