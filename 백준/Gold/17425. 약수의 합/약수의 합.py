import sys

# 입력값보다 작거나 같은 모든 자연수들의 약수의 합

def main(n):
    M = 1_000_001
    dp = [1] * (M)
    for i in range(2, M):
        j = 1
        while i*j <= 1_000_000:
            dp[i*j] += i
            j += 1
    pre_sum = [0] * (M)
    for i in range(1, M):
        pre_sum[i] = pre_sum[i-1] + dp[i]

            

    for i in range(n):
        print(pre_sum[int(input())])
        
        

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    main(n)