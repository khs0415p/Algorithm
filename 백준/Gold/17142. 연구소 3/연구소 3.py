import sys
from itertools import combinations
from copy import deepcopy

def main(n, m):
    board = [list(map(int, input().split())) for _ in range(n)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    def bfs(virus_set):
        cnt = 0
        visited = deepcopy(board)
        
        for x, y in virus_set:
            visited[x][y] = 1
        
        while virus_set:
            tmp = []
            for x, y in virus_set:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == 1: continue
                    
                    visited[nx][ny] = 1
                    tmp.append((nx, ny))
                    
            if not tmp:
                break
            
            # virus 전파 문제
            flag = True
            for check in tmp:
                if check not in virus:
                    flag = False
                    break
            
            if flag and min(map(min, visited)):
                break 
            
            virus_set = tmp
            cnt += 1
            
        if not min(map(min, visited)):
            return float("inf")
        
        return cnt
    
    # 0 빈칸, 1 벽, 2 바이러스
    virus = set()
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                virus.add((i, j))
                
    answer = float("inf")
    
    for virus_set in combinations(virus, m):
        answer = min(answer, bfs(virus_set))
        
    return -1 if answer == float("inf") else answer

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    print(main(n, m))
