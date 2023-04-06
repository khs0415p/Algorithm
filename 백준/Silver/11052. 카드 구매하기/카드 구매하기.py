import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], p[j-1] + dp[i-j])
        
print(dp[-1])
