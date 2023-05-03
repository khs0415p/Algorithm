import sys

def main(n, number):
    
    answer = [-1] * n
    stack = []
    for i in range(n):
        while stack and stack[-1][0] < number[i]:
            answer[stack.pop()[1]] = number[i]
            
        stack.append((number[i], i))
        
    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    number = list(map(int, input().split()))
    print(*main(n, number))