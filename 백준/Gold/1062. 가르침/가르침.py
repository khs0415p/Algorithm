import sys
input = sys.stdin.readline
from itertools import combinations as comb


class Teach():
    def __init__(self, N, K):
        self.answer = 0
        if K == 26:
            self.answer = N
        elif 5 <= K:
            base = set('acint')
            words = [{c for c in input().rstrip()[4:-4] if c not in base} for _ in range(N)]
            all_chars = set()
            for word in words:
                all_chars = all_chars.union(word)
            self.tot_len = len(all_chars)
            if self.tot_len <= K-5:
                self.answer = N
            else:
                atoi = {c: i for i, c in enumerate(all_chars)}
                words = [sum(1<<atoi[c] for c in word) for word in words]
                self.answer = self._teach_words(words, K)
    

    def _teach_words(self, words, K):
        answer = 0
        for seq in comb((1<<i for i in range(self.tot_len)), K-5):
            mask = sum(seq)
            answer = max(answer, sum(mask&word == word for word in words))
        return answer


if __name__ == '__main__':
    teacher = Teach(*map(int, input().split()))
    print(teacher.answer)
