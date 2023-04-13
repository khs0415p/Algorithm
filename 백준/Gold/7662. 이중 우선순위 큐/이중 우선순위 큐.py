import sys
import heapq
def Sol():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        min_heap = []
        max_heap = []
        k = int(input())
        check = [1] * k
        for i in range(k):
            cal, num = input().split()
            num = int(num)
            if cal == "I":
                heapq.heappush(min_heap,(num,i))
                heapq.heappush(max_heap,(-num,i))
            else:    
                if num == -1:
                    if min_heap:
                        check[heapq.heappop(min_heap)[1]] = 0
                elif num == 1:
                    if max_heap:
                        check[heapq.heappop(max_heap)[1]] = 0
            
            while min_heap and check[min_heap[0][1]] == 0:
                heapq.heappop(min_heap)
            while max_heap and check[max_heap[0][1]] == 0:
                heapq.heappop(max_heap)
        if min_heap == []:
            print("EMPTY")
        else:
            print(-max_heap[0][0], min_heap[0][0])

if __name__ == "__main__":
    Sol()