import sys
sys.setrecursionlimit(100_000_000)
from collections import defaultdict

def solution(n, lighthouse):
    graph = defaultdict(set)
    for n1, n2 in lighthouse:
        graph[n1].add(n2)
        graph[n2].add(n1)
        
    def dfs(start):
        
        on, off = 0, 0
        visited[start] = 1
        for node in graph[start]:
            if not visited[node]:
                dfs(node)
                on += min(memo[node])
                off += memo[node][0]
        memo[start] = [on+1, off]
        
    visited = [0] * (n+1)
    memo = [[0, 0] for _ in range(n+1)]
    dfs(1)
    
    return min(memo[1])