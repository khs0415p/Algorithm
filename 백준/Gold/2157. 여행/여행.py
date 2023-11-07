import sys

def main(n, m, k):
    
    paths = [{} for _ in range(n+1)]
    for _ in range(k):
        a, b, c = map(int, input().split())
        if a >= b or c <= paths[a].get(b, 0):
            continue
        paths[a][b] = c
    
    
    memo = {1: 0}
    answer = 0
    for _ in range(m - 1):
        tmp = {}
        for depart, acc in memo.items():
            for arrive, score in paths[depart].items():
                tmp[arrive] = max(acc + score, tmp.get(arrive, 0))
        memo = tmp
        answer = max(answer, memo.get(n, 0))
    
    return answer


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    print(main(n, m, k))