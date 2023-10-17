import sys

def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    dp = [1] * n
    
    # [3, 7, 5, 2, 6, 1, 4]
    # [1, 1, 1, 1, 1, 1, 1]
    # [1, 1, 1, 1, 2, 1, 1]
    # [1, 1, 1, 1, 2, 1, 1]
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(n - max(dp))
    
        

if __name__ == "__main__":
    input = sys.stdin.readline
    solution()
    