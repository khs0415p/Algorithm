import sys
from collections import deque
input = sys.stdin.readline

def main(m, n, k):
    
    board = [[0]*n for _ in range(m)]
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(y1, y2):
            for j in range(x1, x2):
                if board[i][j]: continue
                board[i][j] = -1
    
    group = 0
    total = []
    for i in range(m):
        for j in range(n):
            if not board[i][j]:
                group += 1
                board[i][j] = group
                cnt = 1
                queue = deque([[i,j]])
                while queue:
                    r, c = queue.popleft()
                    for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr >= m or nc < 0 or nc >= n or board[nr][nc] == -1 or board[nr][nc] == group: continue
                        cnt += 1
                        board[nr][nc] = group
                        queue.append([nr, nc])
                         
                total.append(cnt)
    total.sort()
    print(group)
    print(*total)

if __name__ == "__main__":
    m, n, k = map(int, input().split())
    main(m, n, k)
    
    