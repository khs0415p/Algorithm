import sys

def main(target):
    scores = [1, 2, 3]
    dp = [0] * (target + 1)
    
    for score in scores:
        if score > target: continue
        dp[score] += 1
        for i in range(score+1, target+1): 
            dp[i] += dp[i-score]
    return dp[-1]

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        print(main(int(input())))