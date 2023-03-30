def solution(e, starts):
    #  e 10000000
    # s 1 5 10 100 100 억억단에서 가장 많이등장한 수 중 가장 작은 수
    _min = min(starts)
    _dir = [0 for _ in range(e + 1)]
    for i in range(1, e + 1):#횟수 디렉토리
        for j in range(i, e + 1):            
            gu = i * j
            if gu >= e + 1:
                break
            else:
                if i == j :
                    _dir[gu] += 1    
                else :
                    _dir[gu] += 2
    #최대값 역순
    maxnum = 0
    check = [0 for _ in range(e + 1)]
    for z in range(e, 0, -1): 
        if _dir[z] >= maxnum:
            maxnum = _dir[z]
            check[z] = z
        else:
            
            check[z] = check[z + 1]
    
    result = []
    for start in starts:
        result.append(check[start])
        
    return result