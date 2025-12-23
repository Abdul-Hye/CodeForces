a=input().lower()
x=[]
for i in a:
  if i not in x:
    x.append(i)
if len(x)%2==0:
  print( "CHAT WITH HER!")
else:
  print("IGNORE HIM!")