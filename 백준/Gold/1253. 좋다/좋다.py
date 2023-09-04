import sys

def main(n):
    arr = list(map(int, input().split()))
    arr.sort()
    answer = 0
    for i in range(n):
        cur = arr[i]
        temp = arr[:i] + arr[i+1:]
        left, right = 0, n - 2
        # [2, 5]
        while left < right:
            num = temp[left] + temp[right]
            if num > cur:
                right -= 1
            elif num < cur:
                left += 1
            else:
                answer += 1
                break

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    print(main(n))