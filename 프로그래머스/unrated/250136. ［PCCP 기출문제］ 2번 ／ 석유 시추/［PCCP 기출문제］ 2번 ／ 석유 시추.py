from collections import defaultdict

def solution(land):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n, m = len(land), len(land[0])
    
    def bfs(row, col):
        count = 1
        queue = [[row, col]]
        land[row][col] = 0
        cols = set()
        cols.add(col)
        while queue:
            tmp = []
            for r, c in queue:
                for i in range(4):
                    nx, ny = r + dx[i], c + dy[i]
                    if 0 > nx or 0 > ny or nx >= n or ny >= m or land[nx][ny] == 0: continue
                    land[nx][ny] = 0
                    tmp.append([nx, ny])
                    cols.add(ny)
                    count += 1
            queue = tmp
            
        for col in cols:
            answer[col] += count
            
    
    answer = defaultdict(int)
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                bfs(i, j)
                
     
    return max(answer.values())