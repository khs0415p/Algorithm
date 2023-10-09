import sys

def solution():
    n = int(input())
    buildings = list(map(int, input().split()))
    
    result = 0
    for i in range(n):
        pivot = buildings[i]
        
        r_count = 0
        right_prev = float("-inf")
        for j in range(i + 1, n):
            dx = j - i
            dy = buildings[j] - pivot
            gradient = dy/dx
            if right_prev < gradient:
                r_count += 1
                right_prev = gradient
                
        l_count = 0
        left_prev = float("-inf")
        for j in range(i - 1, -1, -1):
            dx = j - i
            dy = pivot - buildings[j]
            gradient = dy/dx
            if left_prev < gradient:
                l_count += 1
                left_prev = gradient
        
        if (l_count + r_count) > result:
            result = (l_count + r_count)
        
    
    return result
    


if __name__ == "__main__":
    input = sys.stdin.readline
    print(solution())