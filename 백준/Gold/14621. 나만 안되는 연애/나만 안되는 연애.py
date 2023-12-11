import sys

def main(n, m, gender):
    
    parent = [i for i in range(n + 1)]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        
        else:
            parent[a] = b


    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]
    
    graph = []
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph.append((c, u, v))
    
    graph.sort()
    
    check = 0
    answer = 0
    for i in range(m):
        c, u, v = graph[i]
        if find(u) != find(v) and gender[u-1] != gender[v-1]:
            union(u, v)
            check += 1
            answer += c
    if check == n - 1:
        print(answer)
    else:
        print(-1)
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    gender = list(input().split())
    main(n, m, gender)