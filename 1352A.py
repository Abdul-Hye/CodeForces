t = int(input())
 
for _ in range(t):
    n = input().strip()
    round_numbers = []
    count = 0
 
    for i in range(len(n) - 1, -1, -1):
        digit = int(n[i])
 
        if digit != 0:
            round_numbers.append(digit * 10**(len(n) - i - 1))
            count += 1
 
    print(count)
    print(' '.join(map(str, round_numbers)))