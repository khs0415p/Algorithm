from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 길 만들기
    
    roads = set()
    area = set()
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, rect)
        
        
        # 제거
        temp = set()
        for y, x in roads:
            if x1 < x < x2 and y1 < y < y2:
                temp.add((y, x))
        # print(sorted(temp), sorted(roads))
        roads -= temp
        
        
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                if i == y1 or i == y2 or j == x1 or j == x2:
                    if (i, j) not in area:
                        roads.add((i, j))
                    
                area.add((i, j))
        
    # bfs 탐색하기
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque([[characterY*2, characterX*2, 0, [(characterY*2, characterX*2)]]])
    
    # 이어진칸 처리
    while queue:    
        y, x, cnt, visited = queue.popleft()
        if x == itemX*2 and y == itemY*2:
            return cnt // 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (ny, nx) in roads and (ny, nx) not in visited:
                queue.append([ny, nx, cnt + 1, visited + [(ny, nx)]])
        
    return -1