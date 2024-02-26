def solution(targets):
    
    targets.sort(key = lambda x:x[-1])
    
    answer = 0
    prev = -1
    for s, e in targets:
        if prev <= s:
            answer += 1
            prev = e
        
    
    return answer