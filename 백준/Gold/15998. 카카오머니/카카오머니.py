import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    
num = int(sys.stdin.readline())
sequence = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]
account = 0
flag = False
charges = []
max_res = 0
for trans, res in sequence:
    if account + trans >= 0:
        if account + trans != res:
            flag = True
            break
        account = res
        
    else:
        total_money = res - account - trans
        charges.append(total_money)
        max_res = max(max_res, res)
        account = res

if flag:
    print(-1)

elif not charges:
    print(1)
    
else:
    value = charges[0]
    
    for c in charges:
        value = gcd(value, c)
    if value > max_res:
        print(value)
        
    else:
        print(-1)
    
