def solution(n):
    answer = [0, 3, 11]
    if n % 2 :
        return answer[0]
    
    if n <= 4:
        return answer[n//2]
    
    for i in range(6, n+1, 2):
        idx = (i - 2)//2
        answer.append((3 * answer[idx] + sum(answer[:idx]) * 2 + 2) % 1000000007)
        
    return answer[n//2]
