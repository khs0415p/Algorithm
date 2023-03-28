from collections import defaultdict, deque
from itertools import combinations
import sys


n = int(sys.stdin.readline().strip())
people = list(map(int,sys.stdin.readline().split()))
graph = defaultdict(set)
answer = float("inf")


       
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for end in temp[1:]:
        graph[i+1].add(end)
        
def bfs(comb):
    queue =  deque([comb[0]])
    visited = set([comb[0]])
    total = 0
    while queue:
        cur_node = queue.popleft()
        total += people[cur_node-1]
        for node in graph[cur_node]:
            if node in comb and node not in visited:
                queue.append(node)
                visited.add(node)
                
    return total, len(visited)

total = sum(people)
for i in range(1, n//2+1):    
    for comb in combinations(range(1,n+1), i):
        sum1, v1 = bfs(comb)
        sum2, v2 = bfs([i for i in range(1, n+1) if i not in comb])
        if v1 + v2 == n:
            answer = min(answer, abs(sum1 - sum2))
            
if answer == float("inf"):
    print(-1)
else:
    print(answer)