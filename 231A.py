n=int(input())
a=[]
count=0
for i in range(n):
  li=[]
  s=input().split(' ')
  a.append(s)
 
for i in a:
  sum=0
  for j in range (len(i)):
    sum+=int(i[j])
  if sum>=2:
    count+=1
print(count)
  