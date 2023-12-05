from collections import deque
import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

K = int(input())
col, row = map(int, input().split())
visited = [[[0]*(K+1) for _ in range(col)] for _ in range(row)]
matrix = [list(map(int, input().split())) for _ in range(row)]

knight = {'a': (-2,-1), 'b': (-1,-2), 'c':(2,1), 'd':(1,2),'e': (-2,1), 'f': (-1,2), 'g':(2,-1), 'h':(1,-2),
        'left': (-1,0), 'right': (1,0), 'top': (0,-1), 'bottom': (0,1)}

def bfs():
    
    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = 1

    while queue:
        cur_r, cur_c, cur_k = queue.popleft()    

        if (cur_r, cur_c) == (row-1, col-1):
            return visited[cur_r][cur_c][cur_k] - 1

        
        for key, value in knight.items():
            nxt_r = cur_r + value[0]
            nxt_c = cur_c + value[1]
            nxt_k = cur_k
            if key not in ['left', 'right', 'top', 'bottom']:
                if cur_k == K:
                    continue
                nxt_k += 1
                
            if 0 <= nxt_r < row and 0 <= nxt_c < col and not matrix[nxt_r][nxt_c] and not visited[nxt_r][nxt_c][nxt_k]:
                visited[nxt_r][nxt_c][nxt_k] = visited[cur_r][cur_c][cur_k] + 1
                queue.append((nxt_r, nxt_c, nxt_k))

    return -1


print(bfs())
