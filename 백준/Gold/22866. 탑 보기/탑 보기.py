import sys

def main(n):
    buildings = list(map(int, input().split()))
    count = [0] * n
    near = [float("inf")] * n
    
    left = []
    for i, h in enumerate(buildings):
        while left and buildings[left[-1]] <= h:
            left.pop()    
        count[i] += len(left)
        
        
        if left:
            if abs(i - left[-1]) < abs(near[i] - i):
                near[i] = left[-1]
        left.append(i)    
        
    right = []
    for i in range(n-1, -1, -1):
        while right and buildings[right[-1]] <= buildings[i]:
            right.pop()
        count[i] += len(right)
        
        if right:
            if abs(right[-1] - i) < abs(near[i] - i):
                near[i] = right[-1]
                
        right.append(i)
    
    
    for c, n in zip(count, near):
        if c > 0:
            print(c, n + 1)
        else:
            print(c)
    


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    main(n)