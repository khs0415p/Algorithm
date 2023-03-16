from sys import stdin
from collections import defaultdict
import heapq

n, e = map(int,stdin.readline().split())
info = [[1,2,3],[2,3,3],[3,4,1],[1,3,5],[2,4,5],[1,4,4]]

graph = defaultdict(list)
for _ in range(e) :
    a,b,c = map(int,stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
a, b = map(int,stdin.readline().split())



def dijkstra(start):
    
    dist = [float("inf")] * (n+1)
    dist[start] = 0
    heap = [[0, start]]
    
    while heap:
        cost, cur_node = heapq.heappop(heap)
        
        if cost > dist[cur_node]:
            continue
        
        for nxt_node, nxt_cost in graph[cur_node]:
            if dist[nxt_node] > cost + nxt_cost:
                dist[nxt_node] = cost + nxt_cost
                heapq.heappush(heap, [cost+nxt_cost, nxt_node])
        
    return dist

a_dist = dijkstra(a)
b_dist = dijkstra(b)
res = min(a_dist[1] + a_dist[b] + b_dist[n], b_dist[1] + b_dist[a] + a_dist[n])

if res >= float("inf"):
    print(-1)
else:
    print(res)
