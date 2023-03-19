n = int(input())
def check(word):
    # 1231
    for i in range(1, len(word)//2+1):
        if word[-2*i:-1*i] == word[-1*i:]:
            return False
        
    return True

candidates = ['3', '2', '1']
stack = []
stack.append('1')

while stack:
    cur_seq = stack.pop()
    if len(cur_seq) == n:
        print(cur_seq)    
        break
    
    for i in range(3):
        temp = cur_seq + candidates[i]
        
        if check(temp):
            stack.append(temp)