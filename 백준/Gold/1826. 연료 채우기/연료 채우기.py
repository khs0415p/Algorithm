import sys
import heapq

def main(n):
    maps = [list(map(int, input().split())) for _ in range(n)]
    target, fuel = map(int, input().split())
    maps.sort()
    
    
    heap = []
    answer = 0
    for i in range(len(maps)):
        if fuel < maps[i][0]:
            while heap:
                fuel -= heapq.heappop(heap)
                answer += 1
                if fuel >= maps[i][0]:
                    break
                
        if fuel >= maps[i][0]:
            heapq.heappush(heap, -maps[i][1])
        
        else:
            return -1
        
    while heap and fuel < target:
        fuel -= heapq.heappop(heap)
        answer += 1
        
        if fuel >= target:
            return answer
    
        
    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    print(main(n))
