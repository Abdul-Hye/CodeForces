a=input()
b=a[0]
c=a[1:]
if 65<=ord(b)<=90:
  print(a)
else:
  d=chr(ord(b)-32)+c
  print(d)