import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
horses = [[2, -1], [2, 1], [1, -2], [1, 2], [-2, -1], [-2, 1], [-1, 2], [-1, -2]]

visited = [[k+1] * w for _ in range(h)]
queue = deque([[0, 0, 0, 0]])

flag = False
while queue:
    cur_x, cur_y, cur_k, cur_cnt = queue.popleft()
    
    if cur_x == (h-1) and cur_y == (w-1):
        flag = True
        break
    
    if cur_k < k:
        for dx, dy in horses:
            nx, ny = cur_x + dx, cur_y + dy
            if 0 > nx or 0 > ny or h <= nx or w <= ny: continue
            if board[nx][ny] or visited[nx][ny] <= cur_k + 1: continue
            visited[nx][ny] = cur_k + 1
            queue.append([nx, ny, cur_k + 1, cur_cnt + 1])
            
    for dx, dy in moves:
        nx, ny = cur_x + dx, cur_y + dy

        if 0 > nx or 0 > ny or h <= nx or w <= ny: continue
        if board[nx][ny] or visited[nx][ny] <= cur_k: continue        
        visited[nx][ny] = cur_k
        queue.append([nx, ny, cur_k, cur_cnt + 1])

if flag:
    print(cur_cnt)
else:
    print(-1)