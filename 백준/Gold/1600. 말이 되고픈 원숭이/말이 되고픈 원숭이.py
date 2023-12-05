import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
horses = [[2, -1], [2, 1], [1, -2], [1, 2], [-2, -1], [-2, 1], [-1, 2], [-1, -2]]
visited = [[k+1] * w for _ in range(h)]

def bfs():
    queue = [[0, 0, 0, 0]]
    while queue:
        tmp = []
        for cur_x, cur_y, cur_k, cur_cnt in queue:
            if cur_x == (h-1) and cur_y == (w-1):
                return cur_cnt
                
        
            if cur_k < k:
                for dx, dy in horses:
                    nx, ny = cur_x + dx, cur_y + dy
                    if 0 > nx or 0 > ny or h <= nx or w <= ny: continue
                    if board[nx][ny] or visited[nx][ny] <= cur_k + 1: continue
                    visited[nx][ny] = cur_k + 1
                    tmp.append([nx, ny, cur_k + 1, cur_cnt + 1])
                
            for dx, dy in moves:
                nx, ny = cur_x + dx, cur_y + dy

                if 0 > nx or 0 > ny or h <= nx or w <= ny: continue
                if board[nx][ny] or visited[nx][ny] <= cur_k: continue
                visited[nx][ny] = cur_k
                tmp.append([nx, ny, cur_k, cur_cnt + 1])
            
        queue = tmp
    return -1

print(bfs())