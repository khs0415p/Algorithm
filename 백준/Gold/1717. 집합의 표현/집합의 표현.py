import sys
sys.setrecursionlimit(10**6)



def find(a):
    if table[a] == a:
        return a
    table[a] = find(table[a])
    return table[a]

def union(a, b):
    a = find(a)
    b = find( b)
    if a < b:
        table[b] = a
    else:
        table[a] = b
    

def main(n, m):
    
    for _ in range(m):
        com, u, v = map(int, input().split())
        if com:
            a, b = find(u), find(v)
            if a == b:
                print("YES")
            else:
                print("NO")
        else:
            union(u, v)
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    table = [i for i in range(n+1)]
    main(n, m)