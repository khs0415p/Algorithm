import sys
from collections import deque
input = sys.stdin.readline

def main(n):
    schedule = [tuple(map(int, input().split())) for _ in range(n)]
    schedule.sort(key = lambda x:[x[-1], x[0]])
    
    cnt = 1
    cur_time = schedule[0][-1]
    for i in range(1, n):
        s, e = schedule[i]
        if cur_time <= s:
            cnt += 1
            cur_time = e
    
    return cnt

if __name__ == "__main__":
    n = int(input())
    print(main(n))
    
    