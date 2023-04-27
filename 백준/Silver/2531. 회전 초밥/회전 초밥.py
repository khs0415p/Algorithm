from sys import stdin

input = stdin.readline
N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr = arr + arr[:k]
memo = [0] * (d + 1)
count = 0
answer = 0
for i in range(k - 1):
    memo[arr[i]] += 1
    if memo[arr[i]] == 1:
        count += 1
for i in range(k - 1, len(arr)):
    memo[arr[i]] += 1
    if memo[arr[i]] == 1:
        count += 1
    answer = max(answer, count + (not bool(memo[c])))
    memo[arr[i - k + 1]] -= 1
    if memo[arr[i - k + 1]] == 0:
        count -= 1
print(answer)