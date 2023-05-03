import sys

def main(n):
    
    balls = []
    for i in range(n):
        c, s = map(int, input().split())
        balls.append((s, c, i))
    balls.sort()
    
    stack = []
    total = prev = 0
    answer = [0] * n
    color_sum = [0] * (n + 1)
    for i in range(n):
        size, color, index = balls[i]
        if size == prev:
            answer[index] = total - color_sum[color]
            stack.append((size, color))
            continue
        
        for s_s, s_c in stack:
            total += s_s
            color_sum[s_c] += s_s
        
        stack = [(size, color)]
        answer[index] = total - color_sum[color]
        prev = size
    print(*answer, sep='\n')
            
            
        
    
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    main(n)