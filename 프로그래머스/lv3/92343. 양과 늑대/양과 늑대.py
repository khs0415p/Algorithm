from collections import defaultdict

def solution(info, edges):
    answer = 0
    
    def dfs(sheep, wolf):
        nonlocal answer
        
        if sheep <= wolf:
            return
        
        answer = max(answer, sheep)
        
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                dfs(sheep + (info[c]==0), wolf + (info[c]==1))
                visited[c] = 0
                
        
        
    visited = [0] * (len(info))
    visited[0] = 1
    dfs(1, 0)
    return answer