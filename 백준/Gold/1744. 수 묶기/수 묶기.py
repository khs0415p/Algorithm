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
        ones += (pos.pop() * pos.pop())
        
        
    while len(neg) > 1:
        ones += (neg.pop() * neg.pop())
        
    
    return ones + (pos[0] if pos else 0) + (neg[0] if neg else 0)
    



if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    print(main(n))