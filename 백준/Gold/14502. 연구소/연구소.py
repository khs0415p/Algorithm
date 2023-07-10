import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
# 8 10
def main(n, m):
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    answer = 0
    def bfs(subset):
        nonlocal answer
        c_board = deepcopy(board)
        
        # 벽
        for sub in subset:
            c_board[sub[0]][sub[1]] = 1
            
        # 바이러스
        for i in range(n):
            for j in range(m):
                if c_board[i][j] == 2:
                    queue = deque([[i, j]])
                    while queue:
                        r, c = queue.popleft()
                        for k in range(4):
                            nr, nc = r + dx[k], c + dy[k]
                            if nr < 0 or nr >= n or nc < 0 or nc >= m or c_board[nr][nc] != 0: continue
                            c_board[nr][nc] = 2
                            queue.append((nr, nc))

        total = 0
        for row in c_board:
            total += row.count(0)
        answer = max(answer, total)
            

    
    def comb(start, wall_length,  subset):
        if len(subset) == 3:
            bfs(subset)
            return
        
        for i in range(start, wall_length):
            comb(i+1, wall_length, subset + [p_wall[i]])
    
    p_wall = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 0]
    comb(0, len(p_wall), [])
    
    return answer

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(main(n, m))