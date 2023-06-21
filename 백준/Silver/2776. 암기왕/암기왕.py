# 1
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5 | 1 1 0 0 1
# 1 1 1 1 1
# 1 2 3 4 5
import sys
input = sys.stdin.readline

def bs(left, right, truth, c):
    # print("c",c)
    while left <= right:
        mid = (left + right) // 2
        if truth[mid] > c:
            right = mid - 1
            
        elif truth[mid] < c:
            left = mid + 1
            
        else:
            return 1 
    return 0

for _ in range(int(input())):
    t_len = int(input())
    truth = list(map(int, input().split()))
    truth.sort()
    c_len = int(input())
    check = list(map(int, input().split()))
    # 4 1 5 2 3
    # 1 2 3 4 5
    # 1 3 7 9 5
    for c in check:
        left, right = 0, t_len-1
        print(bs(left, right, truth, c))
#
        
    
