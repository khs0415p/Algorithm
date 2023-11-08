import sys

def main(n, k):
    graph = [list(map(int, input().split())) for _ in range(n)]
    for m in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][m] + graph[m][j])
    
    def dfs(x, visited, time):
        nonlocal answer
        
        if sum(visited) == n:
            answer = min(answer, time)
        
        for i, nxt in enumerate(graph[x]):
            if not visited[i]:
                visited[i] = 1
                dfs(i, visited, time + nxt)
                visited[i] = 0
                
    visited = [0] * n
    visited[k] = 1
    answer = float("inf")
    dfs(k, visited, 0)
    
    return answer


if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    print(main(n, k))