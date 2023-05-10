import sys

def main(n, m, cap):
    
    
    delivery = [list(map(int, input().split())) for _ in range(m)]
    delivery.sort(key=lambda x:x[1])
    
    
    check = [cap] * (n+1)
    answer = 0
    for i in range(m):
        u, v, c = delivery[i]
        flag = min(min(check[u:v]), c)
        if flag <= 0: continue
        answer += flag
        for j in range(u, v):
            check[j] -= flag
            
            
                
    return answer
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n, cap = map(int, input().split())
    m = int(input())
    print(main(n, m, cap))

     