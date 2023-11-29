import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

count = [0] * (n + 1)
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    count[b] += 1
    
queue = []
for i in range(1, n+1):
    if not count[i]:
        queue.append(i)

answer = []
while queue:
    tmp = []
    for num in queue:
        answer.append(num)
        for nxt in graph[num]:
            count[nxt] -= 1
            if count[nxt] == 0:
                tmp.append(nxt)
    queue = tmp
    
print(*answer)