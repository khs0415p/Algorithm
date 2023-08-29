import sys

def main(n):
    
    graph = [[] for _ in range(n+1)]
    for _ in range(n):
        info = list(map(int, input().split()))
        length = len(info[1:-1])
        for i in range(0, length, 2):
            graph[info[0]].append((info[i+1], info[i+2]))
    
    def dfs(node, visited):
        for next_node, dist in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + dist
                dfs(next_node, visited)
    
    visited = [-1] * (n+1)
    visited[1] = 0
    dfs(1, visited)
    start = visited.index(max(visited))
    visited = [-1] * (n+1)
    visited[start] = 0
    dfs(start, visited)
    
    return max(visited)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    print(main(n))