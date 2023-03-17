import sys
input = sys.stdin.readline

# 최소 신장 트리 ( 사이클 : 유니온 파인드로 확인 )
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

while True:
    n,e = map(int, input().split())
    if not n+e:
        break
    parent = [i for i in range(n)]
    graph = sorted([list(map(int, input().split())) for _ in range(e)], key = lambda x:x[-1])
    answer = 0
    total = 0
    for g in graph:
        a, b, c = g
        total += c
        
        a = find(a)
        b = find(b)
        if a != b:
            union(a, b)
            answer += c
    print(total - answer)
