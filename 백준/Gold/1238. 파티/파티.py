import sys
from collections import defaultdict
import heapq

def main(n, m, x):
    
    # n : 마을
    # m : 길
    # x : 파티 장소
    
    def dijkstra(start):
        distance = [float("inf")] * (n+1)
        distance[start] = 0
        
        queue = [[0, start]]
        while queue:
            dist, node = heapq.heappop(queue)
            
            if distance[node] < dist: continue
            
            for nn, nc in graph[node]:
                ndist = dist + nc
                if distance[nn] > ndist:
                    distance[nn] = ndist
                    heapq.heappush(queue, [ndist, nn])
        
        return distance
    
    graph = defaultdict(list)
    for _ in range(m):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))
    
    answer = 0
    come = dijkstra(x)
    for i in range(1, n+1):
        if i != x:
            
            answer = max(answer, dijkstra(i)[x] + come[i])
            
    return answer
        


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, x = map(int, input().split())
    print(main(n, m, x))