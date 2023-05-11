import sys
sys.setrecursionlimit(10**6)

def find(table, a):
    if table[a] == a:
        return a
    table[a] = find(table, table[a])
    return table[a]

def union(table, a, b):
    a = find(table, a)
    b = find(table, b)
    if a < b:
        table[b] = a
    else:
        table[a] = b
    

def main(n, m):
    
    table = [i for i in range(n+1)]    
    for _ in range(m):
        com, u, v = map(int, input().split())

        if com:
            a, b = find(table, u), find(table, v)
            if a == b:
                print("YES")
            else:
                print("NO")
        else:
            union(table, u, v)
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    main(n, m)