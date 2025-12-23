a=[]
for i in range(5):
  n=input().split()
  a.append(n)
for i in range(len(a)):
  for j in range(len(a)):
    if a[i][j]=='1':
      print(abs(3 - (i + 1)) + abs(3 - (j + 1)))
      break