import sys


def main(n, e):
    
    def union(n1, n2):
        
        a = find(n1)
        b = find(n2)
        if a < b:
            table[b] = a
        else:
            table[a] = b
        
    
    def find(n):
        if n == table[n]:
            return n
        table[n] = find(table[n])
        return table[n]
    
    table = [i for i in range(n+1)]
    graph = [list(map(int, input().split())) for _ in range(e)]
    graph.sort(key = lambda x:x[-1])
    
    cnt = 0
    answer = 0
    for n1, n2, cost in graph:
        
        if find(n1) != find(n2):
            union(n1, n2)
            answer += cost
            cnt += 1
            
    
    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    
    
    n, e = map(int, input().split())
    print(main(n, e))
    