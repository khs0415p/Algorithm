import sys
import bisect
input = sys.stdin.readline

def main(n, m, l):
    places = list(map(int, input().split()))
    length = len(places)
    places.sort()
    cnt = 0
    
    for _ in range(m):
        a, b = map(int, input().split())
        idx = bisect.bisect_left(places, a)
        
        if abs(a - places[idx % length]) + b <= l or abs(a - places[(idx - 1)  % length]) + b <= l or \
        abs(a - places[(idx + 1) % length]) + b <= l:
            cnt += 1
                
    print(cnt)
    
                
            
        

if __name__ == "__main__":
    # n = int(input())
    n, m, l = map(int, input().split())
    main(n, m, l)
    # main(n)