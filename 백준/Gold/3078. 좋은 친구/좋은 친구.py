import sys

def main(n, k):
    
    students = [len(input().rstrip()) for _ in range(n)]
    len_check = [0] * 21
    
    count = 0
    # window
    for i in range(k+1):
        count += len_check[students[i]]
        len_check[students[i]] += 1
        
        
    # move
    for i in range(k+1, n):
        len_check[students[i-k-1]] -= 1
        count += len_check[students[i]]
        len_check[students[i]] += 1
    print(count)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    main(n, k)