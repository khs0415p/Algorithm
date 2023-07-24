import sys
sys.setrecursionlimit(10**6)
def solution(k, room_number):
    
    def find(x):
        if x not in reserverd:
            return x
        reserverd[x] = find(reserverd[x])
        return reserverd[x]
        
    answer = []
    reserverd = {}
    
    for num in room_number:
        if num not in reserverd:
            reserverd[num] = num + 1
            answer.append(num)
        else:
            num = find(num)
            reserverd[num] = num + 1
            answer.append(num)
        
    return answer
# 1,3,4,1,3,1
solution(10, [1,3,4,1,3,1]) # [1,3,4,2,5,6]