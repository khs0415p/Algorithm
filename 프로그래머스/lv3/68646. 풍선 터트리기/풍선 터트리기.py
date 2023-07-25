import heapq

def solution(a):
    
    a = [(ele, i) for i, ele in enumerate(a)]
    right = a[:]
    left = []
    heapq.heapify(right)
    cnt = 0
    for ele, i in a:
        
        if left:
            
            l_ele = left[0][0]
        else:
            
            l_ele = ele + 1
        
        if right:
            
            heapq.heappush(left, (ele, i))
            while right and right[0][1] <= i:
                heapq.heappop(right)
                
            if right:
                r_ele = right[0][0]
            else:
                r_ele = ele + 1
        else:
            r_ele = ele + 1
            
        m_value = max(r_ele, l_ele)
        if m_value > ele:
            cnt += 1
        
    return cnt