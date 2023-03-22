n = int(input())
infos = [list(map(int, input().split())) for _ in range(n*n)]

maps = [[0]*n for _ in range(n)]
dic = {}
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for info in infos:
    dic[info[0]] = info[1:]
    
for info in infos:
    s = info[0]
    candidates = []
    for i in range(n):
        for j in range(n):
            if not maps[i][j]:
                empty = 0
                like = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if not maps[nx][ny]:
                            empty += 1
                    
                        elif maps[nx][ny] in dic[s]:
                            like += 1

                candidates.append((like, empty, -i, -j))
    
    
    l, e, x, y = max(candidates)
    maps[-x][-y] = s
    
scores = [0, 1, 10, 100, 1000]
answer = 0
for i in range(n):
    for j in range(n):
        like = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] in dic[maps[i][j]]:
                    like += 1
                    
        
        answer += scores[like]

print(answer)