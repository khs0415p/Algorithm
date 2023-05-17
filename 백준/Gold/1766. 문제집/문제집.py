import sys
from collections import defaultdict
import heapq

def main(n, m):
    
    
    # 위상정렬
    is_degree = [0] * (n+1)
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        is_degree[b] += 1
    
    queue = []
    for i in range(1, n+1):
        if not is_degree[i]:
            heapq.heappush(queue, i)

    answer = []
    visited = [0] * (n+1)
    while queue:
        node = heapq.heappop(queue)
        visited[node] = 1
        answer.append(node)
        
        for next_node in graph[node]:
            is_degree[next_node] -= 1
            if is_degree[next_node] == 0 and not visited[next_node]:
                heapq.heappush(queue, next_node)
    
    return answer
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    print(*main(n, m))