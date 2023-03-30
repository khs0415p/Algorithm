import sys

N, L = map(int, sys.stdin.readline().split())
road = [ list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [i for i in range(L+1)]

for i in range(1, L+1):
    dp[i] = min(dp[i], dp[i-1]+1)
    for s, e, c in road:
        if s <= i and e == i and c <= dp[i-1]:
            dp[i] = min(dp[s] + c, dp[i]) 
            

print(dp[-1])
