from collections import deque
"POOPO"
"OOOOO"
"OOOXP"
"OPOPX"
"OOOOO"

def bfs(place):
    users = [(i,j) for i in range(5) for j in range(5) if place[i][j] == "P"]
    for user in users:
        queue = deque([user])
        visited = [[-1]*5 for _ in range(5)]
        visited[user[0]][user[1]] = 0
        while queue:
            x, y = queue.popleft()

            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx > 4 or ny < 0 or ny > 4 or visited[nx][ny] != -1 or place[nx][ny] == 'X': continue

                if place[nx][ny] == 'O':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

                elif place[nx][ny] == "P" and visited[x][y] <= 1:
                    return 0
    return 1

def solution(places):
    result = [bfs(place) for place in places]

    return result