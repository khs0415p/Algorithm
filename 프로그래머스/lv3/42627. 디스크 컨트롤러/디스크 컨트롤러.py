import heapq

def solution(jobs):
    jobs.sort()
    start, end, answer = -1, 0, 0
    heap = []
    i = 0
    while i < len(jobs):
        
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(heap, [job[1], job[0]])
                
        if heap:
            cur = heapq.heappop(heap)
            answer += ((end-cur[1]) + cur[0])
            start = end
            end += cur[0]
            i += 1
        else:
            end += 1
            
        

    return answer//len(jobs)