from collections import defaultdict
import heapq
import sys


def main(n):
    
    graph = defaultdict(list)
    while True:
        try:
            u, v, c = map(int, input().split())
            graph[u].append((v, c))
            graph[v].append((u, c))
        except:
            break
    
    def dijkstra(start):
        distance = [float("inf")] * (n + 1)
        distance[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            cost, node = heapq.heappop(heap)
            for n_node, n_cost in graph[node]:
                n_cost += cost
                if distance[n_node] > n_cost:
                    distance[n_node] = n_cost
                    heapq.heappush(heap, [n_cost, n_node])
        return distance
    
    distance = dijkstra(1)
    max_value = (-1, -1)
    for i in range(1, len(distance)):
        if max_value[0] < distance[i]:
            max_value = (distance[i], i)
    distance = dijkstra(max_value[1])
    
    return max(distance[1:])
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    print(main(n))
    