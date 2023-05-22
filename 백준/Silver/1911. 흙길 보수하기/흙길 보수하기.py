import sys
import math

def main(n, l):
    
    total_count = 0
    
    waters = [tuple(map(int, input().split())) for _ in range(n)]
    waters.sort(key=lambda x:x[0])
    
    w_idx = 0
    for s, e in waters:
        
        if w_idx > e: continue
        
        if w_idx  < s:
            w_idx = s
        
        dist = e - w_idx
        cnt = math.ceil(dist / l)
        total_count += cnt
        w_idx += l * cnt
        
    return total_count
        


if __name__ == "__main__":
    input = sys.stdin.readline
    n, l = map(int, input().split())
    print(main(n, l))
    