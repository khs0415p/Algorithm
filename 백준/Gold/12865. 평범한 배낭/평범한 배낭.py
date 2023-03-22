N, K = map(int, input().split())

items = [tuple(map(int, input().split())) for i in range(N)]
# dp[i] = 무게 i에서 가질 수 있는 최대 가치
dp = [0]*(K+1)
dp[0] = 1
for w,v in items:
    for i in range(K-w, -1, -1):
        if dp[i]:
            dp[i+w] = max(dp[i+w], dp[i]+v)
print(max(dp) - 1)