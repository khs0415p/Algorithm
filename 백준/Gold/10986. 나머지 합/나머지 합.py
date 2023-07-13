import sys
input = sys.stdin.readline

def main(n, m):
    arr = list(map(int, input().split()))
    check_m = [0] * m
    total = 0
    for num in arr:
        total += num
        check_m[total % m] += 1
    
    answer = check_m[0]
    for c_m in check_m:
        answer += (c_m * (c_m - 1)) // 2
        
    return answer
                
            
        

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(main(n, m))