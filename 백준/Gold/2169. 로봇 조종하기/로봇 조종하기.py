import sys

def main(n, m):
    
    mars = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = mars[0][0]
    
    for i in range(1, m):
        dp[0][i] = dp[0][i-1] + mars[0][i]
            
    
    for i in range(1, n):
        
        tmp = dp[i-1][:]
        tmp[0] += mars[i][0]
        for j in range(1, m):
            tmp[j] = max(tmp[j] + mars[i][j], tmp[j-1] + mars[i][j])
        
        dp[i] = tmp
        
        tmp = dp[i-1][:]
        tmp[-1] += mars[i][-1]
        for j in range(m-2, -1, -1):
            tmp[j] = max(tmp[j] + mars[i][j], tmp[j+1] + mars[i][j])
            dp[i][j] = max(dp[i][j], tmp[j])
            
    return dp[-1][-1]
            
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    print(main(n, m))