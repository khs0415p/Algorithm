import sys

def main(n, d, k, c):
    
    
    sushi = [int(input()) for _ in range(n)]
    answer = 0
    coupon = set([c])
    belt = sushi + sushi[:(k-1)]
    for i in range(n):
        k_sushi = set(belt[i: i+k])
        answer = max(answer, len(k_sushi | coupon))
        
    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    n, d, k, c = map(int, input().split())
    print(main(n, d, k, c))
    