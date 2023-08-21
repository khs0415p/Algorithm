from collections import deque

def solution(rc, operations):
    
    inner = deque([deque(row[1:-1]) for row in rc[1:-1]])
    up, down = deque(rc[0][1:-1]), deque(rc[-1][1:-1])
    left, right = deque([row[0] for row in rc[1:-1]]), deque([row[-1] for row in rc[1:-1]])
    up_left, up_right = rc[0][0], rc[0][-1]
    down_left, down_right = rc[-1][0], rc[-1][-1]
    
    for oper in operations:
        if oper[0] == "R":
            
            up.appendleft(up_left)
            right.appendleft(up_right)
            down.append(down_right)
            left.append(down_left)
            
            up_left = left.popleft()
            up_right = up.pop()
            down_right = right.pop()
            down_left = down.popleft()
            
            
        else:
            
            inner.appendleft(up)
            left.appendleft(up_left)
            right.appendleft(up_right)
            
            up_left = down_left
            up_right = down_right
            up = down
            
            down = inner.pop()
            down_left = left.pop()
            down_right = right.pop()
            
    up = [[up_left] + list(up) + [up_right]]
    for i in range(len(inner)):
        up.append([left[i]] + list(inner[i]) + [right[i]])
        
    output = up + [[down_left] + list(down) + [down_right]]
        
    return output