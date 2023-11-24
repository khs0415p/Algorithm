def solution(s):
    
    def main(x):
        
        sequence = []
        tar, ones = 0, 0
        for num in map(int, x):
            if num:
                ones += 1
            
            else:
                if ones <= 1:
                    sequence += [1] * ones + [0]
                    ones = 0
                else:
                    tar += 1
                    ones -= 2
        
        return ''.join(map(str, sequence + [1, 1, 0] * tar + [1] * ones))
        
    
    answer = [main(x) for x in s]
    return answer