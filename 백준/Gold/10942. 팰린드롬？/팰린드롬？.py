import sys

def solution(n):
    dp = [[0] * n for _ in range(n)]
    arr = list(map(int, input().split()))
    for k in range(n):
        for i in range(n - k):
            j = i + k
            
            if i == j:
                dp[i][j] = 1
                continue
            
            if arr[i] == arr[j]:
                if (i+1) == j:
                    dp[i][j] = 1
                    
                # 1 3 : 2
                elif dp[i+1][j-1]:
                    dp[i][j] = 1
                
    for _ in range(int(input())):
        s, e = map(int, input().split())
        print(dp[s-1][e-1])
        
        

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    
    solution(n)