import sys
from collections import deque

def main():
    
    l = int(input())
    cur_x, cur_y = map(int, input().split())
    tar_x, tar_y = map(int, input().split())
    
    knight = [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2)]
    
    visited = [[0] * l for _ in range(l)]
    visited[cur_x][cur_y] = 1
    queue = deque([[cur_x, cur_y, 0]])
    while queue:
        # print(queue)
        x, y, cnt = queue.popleft()
        
        if x == tar_x and y == tar_y:
            return cnt
        
        for dx, dy in knight:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or nx >= l or ny < 0 or ny >= l or visited[nx][ny]: continue
            visited[nx][ny] = 1
            queue.append([nx, ny, cnt + 1])
            
    return -1            
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    
    for _ in range(n):
        print(main())