import sys

def main(n):
    pos, neg, ones = [], [], 0
    for _ in range(n):
        num = int(input())
        
        if num <= 0:
            neg.append(num)
        
        elif num == 1:
            ones += 1
        
        else:
            pos.append(num)
    
    pos.sort()
    neg.sort(reverse=True)
    
    while len(pos) > 1:
        tmp = 1
        for _ in range(2):
            tmp *= pos.pop()
        ones += tmp
        
    while pos:
        ones += pos.pop()
    
    
    while len(neg) > 1:
        tmp = 1
        for _ in range(2):
            tmp *= neg.pop()
        ones += tmp
        
    while neg:
        ones += neg.pop()
    
    return ones
    



if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    print(main(n))