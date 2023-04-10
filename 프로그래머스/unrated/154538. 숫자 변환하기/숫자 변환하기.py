# dp
def solution(x, y, n):
    
    dp = [float("inf")] * (y+1)
    dp[x] = 0
    
    for i in range(x+1, y+1):
        if dp[i - n] != float("inf"):
            dp[i] = min(dp[i], dp[i-n] + 1)
            
        if i%2 == 0 and dp[int(i/2)] != float("inf"):
            dp[i] = min(dp[i], dp[int(i/2)] + 1)
            
        if i%3 == 0 and dp[int(i/3)] != float("inf"):
            dp[i] = min(dp[i], dp[int(i/3)] + 1)
    
    return -1 if dp[y] == float("inf") else dp[y]