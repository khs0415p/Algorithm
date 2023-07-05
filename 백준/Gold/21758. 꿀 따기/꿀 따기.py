n = int(input())
arr = list(map(int, input().split()))
psum = [0] * n

for i in range(n):
    psum[i] = arr[i] + psum[i-1]

# 벌 벌 벌통
answer = 0
for i in range(1, n-1):
    tmp = (psum[-1] - arr[i] - arr[0]) + (psum[-1] - psum[i])
    answer = max(answer, tmp)


# 벌통 벌 벌
for i in range(1, n-1):
    tmp = (psum[-1] - arr[-1] - arr[i]) + (psum[i] - arr[i])
    answer = max(answer, tmp)

# 벌 벌통 벌
for i in range(1, n-1):
    tmp = (psum[i]-arr[0]) + (psum[-1]-psum[i-1]-arr[-1])
    answer = max(answer, tmp)

print(answer)