import sys

def main(n, m):
    
    lamp = [input().rstrip() for _ in range(n)]
    k = int(input())
    k_num = k % 2
    
    answer = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if lamp[i][j] == '0':
                cnt += 1
                
        if cnt > k or cnt % 2 != k_num:
            continue
        
        total = 0
        for h in range(i, n):
            if lamp[i] == lamp[h]:
                total += 1
        answer = max(answer, total)
            
    return answer


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    print(main(n, m))