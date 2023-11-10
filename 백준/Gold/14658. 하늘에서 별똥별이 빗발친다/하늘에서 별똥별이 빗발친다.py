import sys

def main(n, m, l, k):
    
    stars = [list(map(int, input().split())) for _ in range(k)]
    
    answer = 0
    for i in range(k):
        for j in range(k):
            tmp = 0
            for m in range(k):
                if stars[i][0] <= stars[m][0] <= stars[i][0] + l and stars[j][1] <= stars[m][1] <= stars[j][1] + l:
                    tmp += 1
            answer = max(answer, tmp)

    return k - answer


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, l, k = map(int, input().split())
    print(main(n, m, l, k))