import bisect

def solution(stones, k):
    
    left, right = min(stones), max(stones)
    while left <= right:
        mid = (left+right) // 2
        cnt = 0
        for s in stones:
            if s - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt >= k:
                break
        
        if cnt >= k:
            right = mid - 1
        
        else:
            left = mid + 1
        
    
    return left