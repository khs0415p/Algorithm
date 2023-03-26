import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
belts = deque([i, False] for i in arr)
n = 1
zeros = 0
while True:
    belts.appendleft(belts.pop())
    belts[N-1][1] = False
    for i in reversed(range(N-1)):
        if belts[i][1] and belts[i+1][0] > 0 and not belts[i+1][1]:
            belts[i+1][0] -= 1
            belts[i+1][1] = True
            belts[i][1] = False
            if belts[i+1][0] == 0:
                zeros += 1
    belts[N-1][-1] = False

    if belts[0][0] > 0 and not belts[0][1]:
        belts[0][1] = True
        belts[0][0] -= 1
        if belts[0][0] == 0:
            zeros += 1
        
    if zeros >= K:
        break
    
    n += 1
print(n)