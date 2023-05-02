import sys
from collections import defaultdict

def main(n):
    balls = []
    for i in range(n):
        c, w = map(int, input().split())
        balls.append((w, c, i))
    balls.sort()
    
    color_weight = defaultdict(int)
    weight_weight = defaultdict(int)
    prefix_sum = [0] * (n+1)
    res = [0] * (n+1)
    
    for i in range(1, n+1):
        prefix_sum[i] = (prefix_sum[i-1] + balls[i-1][0])
        if i > 0 and balls[i-2][0] == balls[i-1][0] and balls[i-2][1] == balls[i-1][1]:
            res[balls[i-1][2]] = res[balls[i-2][2]]
            
        else:
            res[balls[i-1][2]] = prefix_sum[i-1] - color_weight[balls[i-1][1]] - weight_weight[balls[i-1][0]]
        
        
        color_weight[balls[i-1][1]] += balls[i-1][0]
        weight_weight[balls[i-1][0]] += balls[i-1][0]
    
    for i in range(n):
        print(res[i])   
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    main(n)