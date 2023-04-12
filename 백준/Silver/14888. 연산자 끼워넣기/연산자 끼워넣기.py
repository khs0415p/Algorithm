import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
oper = list(map(int, input().split()))

min_value, max_value = float("inf"), float("-inf")
def dfs(depth, res, op1, op2, op3, op4):
    global min_value, max_value
    if depth == n:
        min_value = min(min_value, res)
        max_value = max(max_value, res)
        return
    
    if op1:
        dfs(depth + 1, res + A[depth], op1-1, op2, op3, op4)
        
    if op2:
        dfs(depth + 1, res - A[depth], op1, op2-1, op3, op4)
        
    if op3:
        dfs(depth + 1, res * A[depth], op1, op2, op3-1, op4)
        
    if op4:
        dfs(depth + 1, int(res / A[depth]), op1, op2, op3, op4-1)
        

dfs(1, A[0], oper[0], oper[1], oper[2], oper[3])
print(max_value)
print(min_value)