n=int(input())
a=[]
for i in range(n):
  s=input()
  a.append(s)
for i in a:
  if len(i)<=10:
    print(i)
  else:
    print(i[0]+str(len(i)-2)+i[len(i)-1])