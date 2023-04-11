from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    
    
    def bfs(start):
        queue = deque([start])
        visited = [-1] * (n+1)
        visited[start] = 0
        
        while queue:
            node = queue.popleft()
            
            for next_node in graph[node]:
                if visited[next_node] == -1:
                    queue.append(next_node)
                    visited[next_node] = visited[node] + 1
        return visited
    
    graph = defaultdict(list)
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
    
    visited = bfs(destination)
        
    return [visited[source] for source in sources]

