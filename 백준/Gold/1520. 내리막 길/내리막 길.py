from sys import stdin


def recur(graph, dp, x, y):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if dp[x][y] >= 0:
        return dp[x][y]
    dp[x][y] = 0
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if graph[x][y] > graph[nx][ny]:
            dp[x][y] += recur(graph, dp, nx, ny)
    return dp[x][y]


N, M = map(int, stdin.readline().split())
graph = [list(map(int, row.split())) for row in stdin.readlines()]
dp = [[-1] * M for _ in range(N)]
dp[-1][-1] = 1
print(recur(graph, dp, 0, 0))