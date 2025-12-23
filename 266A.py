
a=int(input())
n=input()
c=0
for i in range(a-1):
  if n[i]==n[i+1]:
    c+=1
print(c)
