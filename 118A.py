s=input().lower()
a=['a','e','i','o','u','y']
x=''
y=[]
for i in range(len(s)):
  if s[i] not in a:
    x+=s[i]
for i in x:
  y.append('.')
  y.append(i)
for i in y:
  if i!=' ':
    print(i,end='')
