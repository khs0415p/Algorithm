import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

# 가장 가까운 노드를 기록
nearnest = [start] * (n + 1)
distance = [1e9] * (n + 1)

q = [(0, start)]
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    
    for next, nextDist in graph[now]:
        cost = nextDist + dist
        if cost < distance[next]:
            distance[next], nearnest[next] = cost, now
            heapq.heappush(q, (cost, next))
    
ans = []
tmp = end
while tmp != start:
    ans.append(str(tmp))
    tmp = nearnest[tmp]

ans.append(str(start))
ans.reverse()

print(distance[end])
print(len(ans))
print(" ".join(ans))