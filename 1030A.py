n=int(input())
a=[]
 
a.append([int(i) for i in input().split()])
for i in a:
  flag=False
  for j in range(len(i)):
    if i[j]>=1:
      flag=True
      break
  if flag:
    print('HARD')
  else:
    print('EASY')