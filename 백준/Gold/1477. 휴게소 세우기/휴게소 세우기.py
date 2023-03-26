import sys

n,m,l = map(int, sys.stdin.readline().split())
places = [0] + list(map(int, sys.stdin.readline().split())) + [l]
places.sort()
start, end = 1, l-1
res = 0
while start <= end:
    cnt = 0
    mid = (start + end)//2 
    for i in range(1, len(places)):
        if places[i] - places[i-1] > mid:
            cnt += (places[i] - places[i-1] - 1)//mid
    
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        res = mid

print(res)