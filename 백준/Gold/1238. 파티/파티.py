import sys
input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra(b, d):
    pq = [(0, X)]
    while pq:
        t, v = heappop(pq)
        if d[v] < t:
            continue
        for tt, vv in b[v]:
            if d[vv] <= t+tt:
                continue
            d[vv] = t+tt
            heappush(pq, (t+tt, vv))


if __name__ == '__main__':
    INF = sys.maxsize
    N, M, X = map(int, input().split())
    ib = [[] for _ in range(N+1)]
    ob = [[] for _ in range(N+1)]
    iid = [INF] * (N+1)
    ood = [INF] * (N+1)
    iid[X] = ood[X] = 0
    for _ in range(M):
        a, b, t = map(int, input().split())
        ib[b].append((t, a))
        ob[a].append((t, b))
    dijkstra(ib, iid)
    dijkstra(ob, ood)
    print(max(sum(tup) for tup in zip(iid[1:], ood[1:])))