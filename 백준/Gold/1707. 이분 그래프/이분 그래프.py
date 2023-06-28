import sys
from collections import deque

def main(v, e):
    
    graph = {i:set() for i in range(1, v+1)}
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
        
    
    
    visited = [0] * (v+1)
    for i in range(1, v+1):
        queue = deque([[i, 0]])
        visited[i] = 1
        groups = [set(), set()]    
        groups[0].add(i)
        while queue:
            
            node, group = queue.popleft()
            n_group = (group + 1) % 2
            
            for n_node in graph[node]:
                if not visited[n_node]:
                    if graph[n_node] & groups[n_group]:
                        return 'NO'
                    visited[n_node] = 1
                    queue.append([n_node, n_group])
                    groups[n_group].add(n_node)
                    
        
    return 'YES'

    



if __name__ == "__main__":
    input = sys.stdin.readline
    k = int(input())
    for _ in range(k):
        v, e = map(int, input().split())
        print(main(v, e))