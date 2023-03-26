import re

def solution(user_id, banned_id):
    
    banned_id = [ b_id.replace("*", ".") for b_id in banned_id]
    answer = set()
    def dfs(comb, start, visited):
        nonlocal answer
        
        if len(comb) == len(banned_id):
            answer.add(tuple(comb))
            return
        
        for i in range(start, len(user_id)):
            for j in range(len(banned_id)):
                if not visited[j] and re.fullmatch(banned_id[j], user_id[i]):
                    visited[j] = 1
                    dfs(comb + [user_id[i]], i+1, visited)
                    visited[j] = 0
                
        
    visited = [0] * len(banned_id)
    dfs([], 0, visited)
    return len(answer)

