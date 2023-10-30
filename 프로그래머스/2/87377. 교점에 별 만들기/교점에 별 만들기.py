from itertools import combinations

def cal(ex1, ex2):
    
    a, b, c = ex1
    aa, bb, cc = ex2
    
    if (a*bb - aa*b) != 0:
        x = (b*cc - bb*c) / (a*bb - aa*b)
        y = (c*aa - a*cc) / (a*bb - aa*b)
        if x.is_integer() and y.is_integer():
            return int(x), int(y)
    

def solution(line):
    
    points = []
    for (ex1, ex2) in combinations(line, 2):
        point = cal(ex1, ex2)
        
        if point:
            points.append(point)
        
        
    min_x, max_x = float("inf"), float("-inf")
    min_y, max_y = float("inf"), float("-inf")
    for point in points:
        min_x = min(min_x, point[0])
        max_x = max(max_x, point[0])
        min_y = min(min_y, point[1])
        max_y = max(max_y, point[1])
    
    answer = [['.'] * (max_x - min_x + 1) for _ in range((max_y - min_y + 1))]
    
    for x, y in points:
        answer[y - min_y][x - min_x] = '*'
    
    answer.reverse()
    return [''.join(row) for row in answer]