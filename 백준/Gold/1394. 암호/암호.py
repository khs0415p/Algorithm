import sys
number = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()

text_to_num = { t:i for i,t in enumerate(number, 1)}
pow = 1
res = 0
for i in range(len(target)-1, -1, -1):
    res = (res + pow  * text_to_num[target[i]]) % 900528
    pow = (pow * len(number)) %  900528
    
print(res)