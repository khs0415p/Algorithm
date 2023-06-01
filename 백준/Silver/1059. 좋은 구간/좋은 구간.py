import sys
import bisect

def main(size, s, n):
    s.sort()
    idx = bisect.bisect_left(s, n)
    end = s[idx] - 1
    start = 1 if idx == 0 else s[idx - 1] + 1
    
    if end < n: return 0
    
    # 23 24 25 26
    # 6 - 2 = 4
    # 9 - 12
    # 910 911 912 : end - start
    # 1011 1012 : end - n
    
    # 34 - 99
    # 3450 3451 3452 ...
    # 3550 3551 3552 ...
    # 4950 4951 ...
    # 5051 5052 ...
    
    # 910 911 912 = (10 - 9) * (12 - 10 + 1) = 2
    # 1011 1012 : 12 - 10 = 2
    cnt = (n-start) * (end - n + 1) + (end - n)
    
    # 34 - 99
    # 34 99 34 98 ... 34 - n : (end - n)
    # 35 99 35 98 ... 35 - n : (end - n)
    # n - 99
    
    
    return cnt
        


if __name__ == "__main__":
    input = sys.stdin.readline
    size = int(input())
    s = list(map(int, input().split()))
    n = int(input())
    print(main(size, s, n))