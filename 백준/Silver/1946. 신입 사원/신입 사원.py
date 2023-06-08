import sys

def main(m):
    
    arr = [tuple(map(int, input().split()))for _ in range(m)]
    arr.sort()
    
    stack = []
    cnt = m
    for i in range(m):
        if not stack or stack[-1][1] > arr[i][1]:
            stack.append(arr[i])
        
        elif stack[-1][1] < arr[i][1]:
            cnt -= 1
    
    return cnt
        


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        print(main(int(input())))