import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def main(n):
    
    graph = defaultdict(list)
    cost = [0] * (n + 1)
    indegree = [0] * (n + 1)
    for i in range(1, n+1):
        info = list(map(int, input().split()))
        cost[i] = info[0]
        for j in info[1:]:
            if j != -1:
                graph[j].append(i)
                indegree[i] += 1
    
    queue = deque()
    dp = [0] * (n + 1)
    # print(indegree)
    # print(graph)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = cost[i]
            
    # 1 -> 2
    
    while queue:
        node = queue.popleft()
        
        for nxt_node in graph[node]:
            indegree[nxt_node] -= 1
            dp[nxt_node] = max(dp[nxt_node], dp[node] + cost[nxt_node])
            # dp[nxt_node] = dp[node] + cost[nxt_node]
            if indegree[nxt_node] == 0:
                queue.append(nxt_node)
        
    for num in dp[1:]:
        print(num)
                
            
        

if __name__ == "__main__":
    n = int(input())
    main(n)