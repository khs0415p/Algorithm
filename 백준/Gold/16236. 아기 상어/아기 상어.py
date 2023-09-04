import sys
from collections import deque, defaultdict

def main(n):
    board = [list(map(int, input().split())) for _ in range(n)]
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    def bfs(shark_x, shark_y, size):
        candidates = []
        queue = deque([(shark_x, shark_y, 0)])
        visited = [[0] * n for _ in range(n)]
        visited[shark_x][shark_y] = 1
        while queue:
            x, y, dist = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]: continue
                if board[nx][ny] <= size:
                    queue.append((nx, ny, dist + 1))
                    visited[nx][ny] = 1
                    if 0 < board[nx][ny] < size:
                        candidates.append((dist + 1, nx, ny))
            
        return candidates
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                shark_x, shark_y = i, j
                board[i][j] = 0
                break
    
    size = 2
    eat = 0
    time = 0
    while next_loc := bfs(shark_x, shark_y, size):
        dist, shark_x, shark_y = min(next_loc)
        board[shark_x][shark_y] = 0
        eat += 1
        time += dist
        if eat == size:
            size += 1
            eat = 0
                
    return time


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    print(main(n))