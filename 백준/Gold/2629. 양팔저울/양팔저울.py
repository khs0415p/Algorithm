import sys

def main(n, medals, m, balls):
    
    dp = set([0])
    
    for medal in medals:
        tmp = set()
        for i in dp:
            tmp.add(i+medal)
            tmp.add(abs(i-medal))
        dp |= tmp
            
    answer = []
    for ball in balls:
        if ball in dp:
            answer.append("Y")
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
    