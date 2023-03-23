def check(num):
    
    if not num or int(num) in [0,1]:
        return False
    num = int(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0 :
            return False
    return True

def solution(numbers):
    answer = set()
    
    def dfs(per, visited):
        nonlocal answer
        if check(per):
            answer.add(int(per[:]))
            
            
        if len(per) == len(numbers):
            return
        
        for i in range(len(numbers)):
            if i not in visited:
                visited.add(i)
                dfs(per + numbers[i], visited)
                visited.remove(i)
                
    visited = set()
    dfs('', visited)
    return len(answer)