
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    f = a % b
    print(0 if f == 0 else b - f)