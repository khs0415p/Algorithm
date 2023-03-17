import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
da = ['d', 'l', 'r', 'u']


def solution(n, m, x, y, r, c, k):
    
    if (k - abs(x-r) + abs(y-c))%2 or abs(x-r) + abs(y-c) > k:
        return "impossible"
    
    
    def dfs(n, m, x, y, r, c, prev_s, k):
        nonlocal answer
        
        if k < len(prev_s) + abs(x-r) + abs(y-c):
            return
        
        if x == r and y == c and len(prev_s) == k :
            answer = prev_s
            return
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 < nx <= n and 0 < ny <= m and prev_s < answer:
                dfs(n, m, nx, ny, r, c, prev_s + da[i], k)
            
    answer = "z"
    dfs(n, m, x, y, r, c, "", k)
    
    return answer