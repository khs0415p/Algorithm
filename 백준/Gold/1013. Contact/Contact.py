import sys

# 10011 10001101
def check(pattern):
    p_length = len(pattern)
    idx = 0
    while idx < p_length:
        if pattern[idx:].startswith('100') :
            idx += 3
            while idx < p_length and pattern[idx] == '0' :
                idx += 1
                
            if idx >= p_length:
                return 'NO'
            idx += 1
            while idx < p_length and pattern[idx] == '1':
                idx += 1 
                
        elif pattern[idx:].startswith('01'):
            idx += 2
            
        
        elif 2 <= idx and  pattern[idx - 2] == '1' and pattern[idx-1:].startswith('100'):
            idx -= 1
            
            
        else:
            return 'NO'
        
    return 'YES'
    

def main(n):
    for _ in range(n):
        patt = input().rstrip()
        print(check(patt))

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    main(n)