n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
 
a = x[1:]  # Levels Little X can pass
b = y[1:]  # Levels Little Y can pass
 
z = set(a + b)  # Combine and remove duplicates using set
 
if len(z) == n:  # Check if all levels from 1 to n are covered
    print("I become the guy.")
else:
    print("Oh, my keyboard!")