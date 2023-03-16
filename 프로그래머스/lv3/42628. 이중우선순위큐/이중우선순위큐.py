import heapq

def check(heap, target):
    index = -1
    
    for i in range(len(heap)):
        if heap[i] == target:
            index = i
            break
    heap.pop(index)
    

def solution(operations):
    min_queue = []
    max_queue = []
    
    for op in operations:
        cmd, num = op.split()
        if cmd == "I":
            heapq.heappush(min_queue, int(num))
            heapq.heappush(max_queue, -int(num))
            
        elif num == "1":
            if max_queue:
                check(min_queue, -heapq.heappop(max_queue))
            
        else:
            if min_queue:
                check(max_queue, -heapq.heappop(min_queue))
    
    return [-heapq.heappop(max_queue), heapq.heappop(min_queue)] if max_queue else [0,0]