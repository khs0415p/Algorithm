import sys

def main(n, k):
    m = len(n)
    b = 10 ** (m-1)
    
    q = [n]
    for _ in range(int(k)):
        temp = set()
        for num in q:
            num = list(num)
            for i in range(m-1):
                for j in range(i+1, m):
                    num[i], num[j] = num[j], num[i]
                    
                    if int(''.join(num)) >= b:
                        
                        temp.add(''.join(num))
                    num[i], num[j] = num[j], num[i]
        
        q = temp
    
    return max(map(lambda x: int(''.join(x)), q)) if q else -1


if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = input().split()
    print(main(n, k))