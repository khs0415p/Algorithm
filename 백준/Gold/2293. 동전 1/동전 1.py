import sys
sys.setrecursionlimit(10_000)
def main(n, k):
    answer = 0
    scores = [int(input()) for _ in range(n)]
    dp = [0] * (k+1)

    for score in scores:
        if score>k: continue
        dp[score] += 1
        for i in range(score+1, k+1):
            
            dp[i] += dp[i-score]
    
    return dp[-1]

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    print(main(n, k))