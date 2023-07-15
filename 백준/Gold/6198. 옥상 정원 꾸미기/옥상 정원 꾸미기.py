import sys
input = sys.stdin.readline

def main(n):
    buildings = [int(input()) for _ in range(n)]
    stack = []
    answer = [0] * n
    for i, building in enumerate(buildings):
        while stack and stack[-1][0] <= building:
            idx = stack.pop()[1]
            answer[idx] = i - idx - 1
        stack.append([building, i])
        
    while stack:
        idx = stack.pop()[1]
        answer[idx] = n - idx - 1
        
    return sum(answer)
                
            
        

if __name__ == "__main__":
    n = int(input())
    print(main(n))