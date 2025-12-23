n = int(input())

capacity = 0
passengers = 0

for i in range(n):
    a, b = map(int, input().split())
    passengers -= a
    passengers += b
    capacity = max(capacity, passengers)

print(capacity)
