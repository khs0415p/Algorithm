import sys
from collections import deque, defaultdict

def main(n, m):
    
    delay = list(map(int, input().split()))
    graph = defaultdict(list)
    degree = {i:0 for i in range(1, n+1)}
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        degree[e] += 1

    queue = deque([])
    target = int(input())
    dist = [-1] * (n + 1)
    for key in degree.keys():
        if not degree[key]:
            queue.append(key)
            dist[key] = delay[key - 1]
    
    
    while queue:
        node = queue.popleft()
        
        for n_node in graph[node]:
            dist[n_node] = max(dist[n_node], dist[node] + delay[n_node - 1])
            degree[n_node] -= 1
            if not degree[n_node]:
                queue.append(n_node)
    return dist[target]


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    for _ in range(N):
        n, m = map(int, input().split())
        print(main(n, m))