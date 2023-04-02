from collections import defaultdict, deque
import sys

n = int(sys.stdin.readline())
maps = list(map(int, sys.stdin.readline().split()))
delete_node = int(sys.stdin.readline())
tree = defaultdict(list)

for i in range(n):
    tree[maps[i]].append(i)
    tree[i]
    
# 삭제

tree[maps[delete_node]].remove(delete_node)
if maps[delete_node] == -1:
    tree.pop(-1)

childs = tree.pop(delete_node)
for child in childs:
        
    queue = deque([child])
    while queue:
        cur_node = queue.popleft()
    
        for node in tree[cur_node]:
            queue.append(node)
        tree.pop(cur_node)
            
answer = 0
for v in tree.values():
    if not v:
        answer += 1
        
print(answer)