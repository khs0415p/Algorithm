import sys

input = sys.stdin.readline

n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]
min_value = float("inf")

for start in range(3):
    dp = [[float("inf")] * 3 for _ in range(n)]
    dp[0][start] = scores[0][start]
    
    for i in range(1, n):
        dp[i][0] = scores[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = scores[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = scores[i][2] + min(dp[i-1][0], dp[i-1][1])
        
    for end in range(3):
        if start != end:
            min_value = min(min_value, dp[n-1][end])
print(min_value)