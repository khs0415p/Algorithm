import sys
from collections import deque

def main(n, graph):
    
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        queue = deque([i])
        
        while queue:
            node = queue.popleft()
            
            for j, e in enumerate(graph[node]):
                
                if e and not visited[i][j]:            
                    visited[i][j] = 1
                    queue.append(j)
        
    for v in visited:
        print(*v)
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    main(n, graph)