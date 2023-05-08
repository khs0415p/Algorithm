import sys

def main(n, medals, m, balls):
    dp = [0] * 40001
    dp[0] = 1
    for medal in medals:
        for i in range(40000 - medal, -1, -1):
            if dp[i]:
                dp[i+medal] = 1
                
    answer = []
    
    for ball in balls:
        for i in range(40000 - ball):
            if dp[i] and dp[i+ball]:
                answer.append("Y")
                break
        else:
            answer.append("N")
        
    return ' '.join(answer)
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    medals = list(map(int, input().split()))
    m = int(input())
    balls = list(map(int, input().split()))
    print(main(n, medals, m, balls))
    