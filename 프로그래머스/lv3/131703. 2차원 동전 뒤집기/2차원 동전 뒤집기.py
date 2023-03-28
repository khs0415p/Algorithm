def solution(beginning, target):
    from copy import deepcopy
    from collections import deque
    def check(arr, v1, v2):
        flag = 0
        for i in range(len(target)):
            for j in range(len(target[0])):
                if arr[i][j] != target[i][j]: 
                    if v1[i] and v2[j]: return 2
                    flag = 1
        return flag
    answer = 20
    q = deque([[0, 0, 0, deepcopy(beginning), [0] * len(beginning), [0] * len(beginning[0])]])
    while q:
        cnt, i, j, now, v1, v2 = q.popleft()
        flag = check(now, v1, v2)
        if flag == 2: continue
        elif flag == 0: answer = min(answer, cnt)
        if i < len(beginning):
            q.append([cnt, i + 1, j, deepcopy(now), v1[::], v2[::]])
            for y in range(len(beginning[0])):
                now[i][y] = 1 - now[i][y]
            v1[i] = 1
            q.append([cnt + 1, i + 1, j, deepcopy(now), v1[::], v2[::]])        
        elif j < len(beginning[0]):
            q.append([cnt, i, j + 1, deepcopy(now), v1[::], v2[::]])
            for x in range(len(beginning)):
                now[x][j] = 1 - now[x][j]
            v2[j] = 1
            q.append([cnt + 1, i, j + 1, deepcopy(now), v1[::], v2[::]])
    return answer if answer != 20 else -1