# 투포인터
def solution(gems):
    
    length = len(gems)
    answer = [0, length-1]
    check_dic = {gems[0]:1}
    gems_set = set(gems)
    start, end = 0, 0
    
    while start <= end:
        
        if len(check_dic) < len(gems_set):
            end += 1
            if end == length:
                break
            check_dic[gems[end]] = check_dic.get(gems[end], 0) + 1
        
        else:
            # 같다.
            if (end - start) + 1 < (answer[-1] - answer[0]) + 1:
                answer = [start, end]
                
            if check_dic[gems[start]] == 1:
                check_dic.pop(gems[start])
                
            else:
                check_dic[gems[start]] -= 1
            
            start += 1
    
    answer[0] += 1
    answer[1] += 1
        
    return answer