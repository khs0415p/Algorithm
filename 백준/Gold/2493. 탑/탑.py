import sys

def main(n):
    towers = list(map(int, input().split()))
    answer = [0] * n
    # 4 7 5 9 6
    # 7 4 5
    # 5 4 7
    stack = []
    for i in range(len(towers)-1, -1, -1):
        tower = towers[i]
        while stack and towers[stack[-1]] <= tower:
            answer[stack.pop()] = i+1
            
        stack.append(i)
    
    print(*answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    main(n)
    