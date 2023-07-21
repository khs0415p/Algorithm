import sys
from itertools import combinations
input = sys.stdin.readline


def main(n, k):
    
    if k < 5:
        return 0
    
    elif k == 26:
        return n
    
    learned = set('antic')
    words = [set(input().rstrip()[4:-4]) - learned for _ in range(n)]
    
    all_char = set()
    for word in words:
        all_char = all_char.union(word)
        
    if len(all_char) <= (k - 5):
        return n
    
    # bit
    
    ctoi = {c:i for i, c in enumerate(all_char)}
    words = [sum(1 << ctoi[c] for c in word) for word in words]
    comb = []
    def dfs(cnt, subset):
        nonlocal comb
        if cnt == (k - 5):
            comb.append(subset)
            return
        
        if not bit_char:
            return
        
        n = bit_char.pop()
        dfs(cnt + 1, subset + [n])
        dfs(cnt, subset)
        bit_char.append(n)
    bit_char = [1 << ctoi[c] for c in all_char]
    dfs(0, [])
    
    answer = 0
    for seq in comb:
        mask = sum(seq)
        
        answer = max(answer, sum([mask&word == word for word in words]))
                
    return answer
    
    # return all_char

if __name__ == "__main__":
    
    n, k = map(int, input().split())
    print(main(n, k))

