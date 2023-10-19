import sys

def solution():
    
    t = int(input())
    for _ in range(t):
        w = input().rstrip()
        k = int(input())
        
        if k == 1:
            print(1, 1)
            continue
        
        min_value = float("inf") # 4
        max_value = float("-inf") # 4
        check = {}
        for i, c in enumerate(w):
            if c in check:
                check[c].append(i)
                
                if len(check[c]) == k:
                    min_value = min(min_value, check[c][-1] - check[c][0] + 1)
                    max_value = max(max_value, check[c][-1] - check[c][0] + 1)
                    check[c].pop(0)
            
            else:
                check[c] = [i]
        
        if min_value == float("inf") or max_value == float("-inf"):
            print(-1)
            continue
        
        print(min_value, max_value)
            

if __name__ == "__main__":
    input = sys.stdin.readline
    solution()