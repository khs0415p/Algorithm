import math

def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]
    num = n
    
    for _ in range(n):
        m = math.factorial(num - 1)
        idx = (k-1) // m
        k = k % m
        answer.append(arr.pop(idx))
        num -= 1
        
    return answer