import sys
import bisect

def solution(t):
    for i in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        
        temp = [arr[0]]
        for num in arr[1:]:
            if temp[-1] < num:
                temp.append(num)
            else:
                temp[bisect.bisect_left(temp, num)] = num
        
        length = len(temp)
        print(f"Case #{i + 1}")
        if length >= k:
            print(1)
            
        else:
            print(0)
            
                
                
                
        
        
        

if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    solution(t)