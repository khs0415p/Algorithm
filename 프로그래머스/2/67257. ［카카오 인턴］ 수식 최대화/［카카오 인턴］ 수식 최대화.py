import re
from itertools import permutations

def solution(expression):
    
    exp = re.split("([-+*])", expression)
    res = []
    stack = []
    for op in permutations(['-', '+', '*'], 3):
        copy_exp = exp[:]
        for o in op:
            stack = []
            idx = 0
            while idx < len(copy_exp):
                if copy_exp[idx] == o:
                    stack.append(str(eval(stack.pop() + o + copy_exp[idx+1])))
                    idx += 2
                    
                else:
                    stack.append(copy_exp[idx])
                    idx += 1
                
            copy_exp = stack[:]
        res.append(stack[0])
    
    answer = 0
    for r in res:
        answer = max(answer, abs(int(r)))
    return answer