import sys
sys.setrecursionlimit(500_000)


def main(n, m):
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]
    visited[-1][-1] = 1
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def dfs(x, y):
        
        visited[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if board[x][y] > board[nx][ny]:
                visited[x][y] += visited[nx][ny] if visited[nx][ny] != -1 else dfs(nx, ny)
                
        return visited[x][y]
    
    dfs(0, 0)
    return visited[0][0]

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    print(main(n, m))