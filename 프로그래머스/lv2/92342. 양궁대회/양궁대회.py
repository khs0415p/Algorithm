def solution(n, info):
    
    def dfs(n, index, ryan, info):
        nonlocal score, answer
        
        if n < 0 and index == 11:
            
            c_ryan = ryan[:]
            c_ryan[-1] = n + c_ryan[-1]
            s = 0
            for i in range(10):
                if info[i] == 0 and c_ryan[i] == 0 : continue
                
                if info[i] < c_ryan[i]:
                    s += (10 - i)
                else:
                    s -= (10 - i)
            if score <= s:
                score = s
                if score == s and answer[::-1] > c_ryan[::-1]:
                    return
                answer = c_ryan[:]
            return
        
        if n < 0: return
        
        if n == 0:
            s = 0
            
            for i in range(11):
                if info[i] == 0 and ryan[i] == 0: continue
                
                if info[i] < ryan[i]:
                    s += (10 - i)
                else:
                    s -= (10 - i)
            
            if 0 < s and score <= s :
                if score == s and answer[::-1] > ryan[::-1]:
                    return
                answer = ryan[:]
                score = s
            return
        
        for i in range(index, 11):
            if ryan[i] <= info[i]:
                ryan[i] += (info[i] + 1)
                dfs(n - (info[i] + 1), i + 1, ryan, info)
                ryan[i] -= (info[i] + 1)
        
    
    answer = [-1]
    score = 0
    ryan = [0] * 11
    dfs(n, 0, ryan, info)
    return answer