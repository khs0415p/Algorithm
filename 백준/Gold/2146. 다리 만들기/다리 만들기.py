import sys
from collections import deque

input = sys.stdin.readline
# 1:땅 0:바다
n = int(input())
islands = [ list(map(int, input().split())) for _ in range(n)]

island_num = 1
visited = [[0] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(n):
    for j in range(n):
        if islands[i][j] and not visited[i][j]:
            visited[i][j] = 1
            islands[i][j] = island_num
            queue = deque([[i,j]])
            
            while queue:
                x, y = queue.popleft()
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and islands[nx][ny]:
                        visited[nx][ny] = 1
                        islands[nx][ny] = island_num
                        queue.append([nx, ny])
                        
            island_num += 1
            
min_value = float("inf")
for i in range(n):
    for j in range(n):
        if islands[i][j]:
            
            i_id = islands[i][j]
            
            visited = [[0] * n for _ in range(n)]
            visited[i][j] = 1
            
            queue = deque([])
            
            for k in range(4):
                nx , ny = i + dx[k], j + dy[k]
                
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and not islands[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny, 1])
                    
            
            visited = [[0] * n for _ in range(n)]
            
            while queue:
                x, y, dist = queue.popleft()
                
                if visited[x][y] or islands[x][y] == i_id: continue
                visited[x][y] = 1
                
                if islands[x][y] != 0:
                    min_value = min(min_value, dist - 1)
                    queue = []
                    break
                
                for k in range(4):
                    nx , ny = x + dx[k], y + dy[k]    
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] :
                        queue.append([nx, ny, dist + 1])
            
print(min_value)