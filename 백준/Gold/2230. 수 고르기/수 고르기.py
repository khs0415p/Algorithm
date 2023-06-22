import sys

def main(n, m):
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    if len(nums) < 2:
        return nums[0]
    
    if not m:
        return 0
    
    answer = float("inf")
    s, e = 0, 0
    while e < len(nums):
        res = (nums[e] -  nums[s])
        if res >= m:
            answer = min(answer, res)
            s += 1
        
        else:
            e += 1
    
    return answer
    


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    print(main(n, m))