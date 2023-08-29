import sys
input = sys.stdin.readline


class Pairings():
    def __init__(self, N):
        left = [0] * 100
        right = [0] * 100
        mini_maxies = [0] * N
        for i in range(N):
            l, r = map(int, input().split())
            left[l] += 1
            right[r] += 1
            li, ri = 1, 99
            lcnt, rcnt = left[li], right[ri]
            while li <= 99 and ri >= 1:
                while li < 99 and not lcnt:
                    li += 1
                    lcnt = left[li]
                while ri > 1 and not rcnt:
                    ri -= 1
                    rcnt = right[ri]
                if ri == 1 and not rcnt:
                    break
                mini_maxies[i] = max(mini_maxies[i], li+ri)
                if lcnt <= rcnt:
                    rcnt -= lcnt
                    lcnt = 0
                else:
                    lcnt -= rcnt
                    rcnt = 0
        self.answer = mini_maxies


if __name__ == '__main__':
    pairs = Pairings(int(input()))
    print('\n'.join(map(str, pairs.answer)))