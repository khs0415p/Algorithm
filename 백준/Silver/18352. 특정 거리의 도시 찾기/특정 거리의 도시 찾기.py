import sys
from collections import deque
input = sys.stdin.readline

def main(n, m, k, x):
    graph = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
    
    
    queue = deque([[x, 0]])
    visited = [0] * (n+1)
    visited[x] = 1
    answer = []
    while queue:
        node, cnt = queue.popleft()
        if cnt == k:
            answer.append(node)
            continue
        
        for n_node in graph[node]:
            if not visited[n_node]:
                visited[n_node] = 1
                queue.append([n_node, cnt + 1])
            
    answer.sort()
    if not answer:
        print(-1)
        return
    
    for num in answer:
        print(num)
                
            
        

if __name__ == "__main__":
    n, m, k, x = map(int, input().split())
    main(n, m, k, x)