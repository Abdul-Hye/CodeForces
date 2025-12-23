n = int(input())
pi = list(map(int, input().split()))
gift_giver = [0] * n
 
for i in range(1, n+1):
    gift_giver[pi[i-1]-1] = i
 
print(*gift_giver)