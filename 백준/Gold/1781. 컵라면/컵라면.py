import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()

queue = []

for d, c in arr:
    heapq.heappush(queue, c)
    if d < len(queue):
        heapq.heappop(queue)

print(sum(queue))