import sys
from collections import deque
    

def main(n, m):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def search(x, y, group):
        
        count = 1
        queue = deque([[x, y]])
        while queue:
            row, col = queue.popleft()
            for i in range(4):
                nx, ny = row + dx[i], col + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] == '1': continue
                if board[nx][ny] == '0':
                    count += 1
                    queue.append([nx, ny])
                    board[nx][ny] = group
                
        return count
    
    board = [list(input().rstrip()) for _ in range(n)]
    group = 2
    groups = {}
    for i in range(n):
        for j in range(m):
            if board[i][j] == '0':
                board[i][j] = group
                cnt = search(i, j, group)
                groups[group] = cnt
                group += 1
                
    answer = [['0'] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == '1':
                cnt = 1
                check = set()
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] == '1': continue
                    check.add(board[nx][ny])
                
                for key in check:
                    cnt += groups[key]
                
                answer[i][j] = str(cnt % 10)
                
    
    for b in answer:
        print(''.join(b))
                    
                    

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    main(n, m)