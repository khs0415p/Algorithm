def solution(N, number):
        
    if N==number: return 1
    
    dp = [0, {N}]
    for i in range(2, 9):
        
        num_set = set()
        num_set.add(int(str(N) * i))
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    num_set.add(a + b)
                    num_set.add(a - b)
                    num_set.add(b - a)
                    num_set.add(a * b)
                    
                    if a != 0:
                        num_set.add(b // a)
                        
                    if b != 0:
                        num_set.add(a // b)
                    
        if number in num_set:
            return i
        
        dp.append(num_set)
    
    
            
    return -1