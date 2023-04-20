import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
max_value = max(map(max, board))
result = float("-inf")

def dfs(depth, x, y, visited, total):
    global result
    
    if total + max_value * (4-depth) <= result:
        return
    if depth == 4:
        result = max(result, total)
        return
    
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if depth == 2:
                visited[nx][ny] = 1
                dfs(depth + 1, x, y, visited, total + board[nx][ny])
                visited[nx][ny] = 0
                
            visited[nx][ny] = 1
            dfs(depth + 1, nx, ny, visited, total + board[nx][ny])
            visited[nx][ny] = 0

visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(1, i, j, visited, board[i][j])
        visited[i][j] = 0

print(result)