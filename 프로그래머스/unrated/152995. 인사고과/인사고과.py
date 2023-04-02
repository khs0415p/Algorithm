def solution(scores):
    
    pivot = scores[0]
    total = sum(pivot)
    scores.sort(key=lambda x:[-x[0], x[1]])
    
    answer = 1
    ths = 0
    for score in scores:
        if pivot[0] < score[0] and pivot[1] < score[1]:
            return -1
        
        if ths <= score[1]:
            if total < score[0] + score[1]:
                answer += 1
            ths = score[1]
        
    return answer