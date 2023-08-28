import sys
import heapq

def main(n, m):
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
    
    def djikstra(node):
        distance = [float("inf")] * (n + 1)
        distance[node] = 0
        roads = [node] * (n+1)
        
        queue = []
        heapq.heappush(queue, (distance[node], node))
        while queue:
            dist, cur = heapq.heappop(queue)
            if dist > distance[cur]: continue
            for n_node, cost in graph[cur]:
                n_cost = dist + cost
                if distance[n_node] > n_cost:
                    distance[n_node] = n_cost
                    roads[n_node] = cur
                    heapq.heappush(queue, (n_cost, n_node))
                
        return distance, roads
    
    start, end = map(int, input().split())
    distance, roads = djikstra(start)
    
    print(distance[end])
    answer = []
    while end != start:
        answer.append(end)
        end = roads[end]
        
    answer.append(start)
    answer.reverse()
    print(len(answer)) 
    print(*answer)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    main(n, m)