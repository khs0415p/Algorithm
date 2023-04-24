import sys

def main(line):
    
    check = [0] * (n)
    for i in range(1, n):
        if abs(line[i] - line[i-1]) > 1:
            return False
        
        if line[i] > line[i-1]:
            if (i - l) < 0 :
                return False
            
            for j in range(l):
                if line[i-1-j] != line[i-1] or check[i-1-j]:
                    return False
                check[i-1-j] = 1
            
        elif line[i] < line[i-1]:
            if (i + l) > n :
                return False
            
            for j in range(l):
                if line[i+j] != line[i] or check[i+j]:
                    return False
                check[i+j] = 1
    return True

if __name__ == "__main__":
    input = sys.stdin.readline
    n, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for line in board:
        if main(line):
            answer += 1
    
    for line in zip(*board):
        if main(line):
            answer += 1
            
    print(answer)