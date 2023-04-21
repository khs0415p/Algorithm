import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

moves = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
diags = [2, 4, 6, 8]
clouds = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]

for _ in range(M):
    d, s = map(int, input().split())
    # 이동
    dx, dy = moves[d]
    dx *= s
    dy *= s
    
    check_pos = set()
    for i in range(len(clouds)):
        clouds[i][0] = (clouds[i][0] + dx + N * s) % N
        clouds[i][1] = (clouds[i][1] + dy + N * s) % N
        x, y = clouds[i]
        check_pos.add((x, y))
        board[x][y] += 1
    
    # 대각
    for x, y in clouds:
        cnt = 0
        for i in diags:
            dx, dy = moves[i]
            nx = x + dx 
            ny = y + dy
            
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny]:
                cnt += 1
        
        board[x][y] += cnt
    
    # 2 이상 and 구름이 사라진 칸 제외
    next_clouds = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and (i, j) not in check_pos:
                board[i][j] -= 2
                next_clouds.append([i,j])
    
    clouds = next_clouds
    
print(sum([sum(b) for b in board]))
            