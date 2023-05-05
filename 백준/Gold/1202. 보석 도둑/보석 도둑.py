import sys
import heapq

def main(n, k):
    
    juwels = [tuple(map(int, input().split())) for _ in range(n)]
    bags = [int(input()) for _ in range(k)]
    bags.sort()
    juwels.sort(reverse=True)
    
    get = []
    answer = 0
    for bag in bags:
        while juwels and juwels[-1][0] <= bag:
            mass, value = juwels.pop()
            heapq.heappush(get, (-value, mass))
            
        if get:
            answer -= heapq.heappop(get)[0]
             
    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    
    
    print(main(n, k))
    