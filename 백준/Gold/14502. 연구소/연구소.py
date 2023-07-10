import sys
from collections import deque
input = sys.stdin.readline
# 8 10
def main(n, m):
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    answer = 0
    def bfs():
        nonlocal answer
        
        virus = set()
        tmp = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    queue = deque([[i, j]])
                    tmp += 1
                    while queue:
                        # print(queue)
                        r, c = queue.popleft()
                        for k in range(4):
                            nr, nc = r + dx[k], c + dy[k]
                            
                            if nr < 0 or nr >= n or nc < 0 or nc >= m or board[nr][nc] != 0: continue
                            virus.add((nr, nc))
                            board[nr][nc] = 2
                            queue.append((nr, nc))

        total = 0
        for row in board:
            total += row.count(0)
            
        answer = max(answer, total)
        
        for v in virus:
            board[v[0]][v[1]] = 0
            

    
    def comb(cnt):
        if cnt == 3:
            bfs()
            return
        # 중복 제거하는법?
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    board[i][j] = 1
                    comb(cnt + 1)
                    board[i][j] = 0
    
    comb(0)
    
    return answer

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(main(n, m))