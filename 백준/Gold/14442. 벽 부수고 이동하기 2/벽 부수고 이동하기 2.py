from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
maps = [input().rstrip() for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
queue = deque([[0, 0, k, 1]])
visited[0][0][0] = 1
answer = -1

while queue:
        
    x, y, k, cnt = queue.popleft()
    
    if x == n-1 and y == m-1:
        answer = cnt
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][k]:
            visited[nx][ny][k] = 1
            
            if maps[nx][ny] == '0':
                queue.append([nx, ny, k, cnt+1])
                
            elif k:
                queue.append([nx, ny, k-1, cnt+1])

print(answer)