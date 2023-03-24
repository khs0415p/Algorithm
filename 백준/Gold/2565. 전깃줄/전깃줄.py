import sys
import bisect
input = sys.stdin.readline
n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()

arr = []
for s, e in lines:
    if not arr:
        arr.append(e)
        
    else:
        idx = bisect.bisect_left(arr, e)
        if idx == len(arr):
            arr.append(e)
        else:
            arr[idx] = e
print(len(lines) - len(arr))