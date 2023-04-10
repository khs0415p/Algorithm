from collections import deque

n, t = map(int, input().split())
queue = deque([[n, 0]])
visited = [float("inf")] * 100001

while queue:
    num, cnt = queue.popleft()
    
    if visited[num] <= cnt:
        continue
    
    visited[num] = cnt
    if num * 2 < 100001:
        queue.append([num*2, cnt])
        
    if num + 1 < 100001:
        queue.append([num+1, cnt+1])
        
    if num > 0:
        queue.append([num-1, cnt+1])
    
print(visited[t])
    
