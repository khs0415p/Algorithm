import sys
from collections import deque

def main(n, m):
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def bfs(queue):
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                
                if board[nx][ny] == 0:
                    board[nx][ny] = -1
                    queue.append((nx, ny))
    board[0][0] = -1
    bfs(deque([[0, 0]]))
    
    
    time = 0
    while True:
        edge_queue = deque([])
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    check = 0
                    for k in  range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                        if board[nx][ny] == -1:
                            check += 1
                                
                    if check >= 2:
                        edge_queue.append((i, j))
        
        if not edge_queue: break
        
        for x, y in edge_queue:
            board[x][y] = -1
        bfs(edge_queue)
        time += 1 
    
    return time


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    print(main(n, m))