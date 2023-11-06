import sys

def main(n, k):
    
    dp = [[0]*(n+1) for i in range(k + 1)]
    for i in range(n + 1):
        dp[1][i] = 1
    
    for i in range(k+1):
        dp[i][1] = i
        
    for i in range(2, k+1):
        for j in range(2, n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    return dp[k][n] % 1_000_000_000


if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    print(main(n, k))
    
    