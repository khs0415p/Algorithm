def solution(e, starts):
    #  e 10000000
    # s 1 5 10 100 100 억억단에서 가장 많이등장한 수 중 가장 작은 수
    
    check = [1] * (e+1)
    
    for i in range(2, e+1):
        for j in range(i, e+1, i):
            check[j] += 1
            
    result = []
    
    max_list = [0] * (e+1)
    max_num = 0
    for i in range(len(check)-1, 0, -1):
        if check[i] >= max_num:
            max_list[i] = i
            max_num = check[i]
            
        else:
            max_list[i] = max_list[i+1]
        
    return [max_list[start] for start in starts]