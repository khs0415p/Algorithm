def solution(sequence, k):
    answer = [0, len(sequence)-1]
    s, e = 0, -1
    total = 0
    
    for i in range(len(sequence)):
        total += sequence[i]
        e += 1
        
        while total > k:
            total -= sequence[s]
            s += 1
        
        if total == k:
            if (answer[1] - answer[0]) > (e - s):
                answer = [s, e]
    
    return answer