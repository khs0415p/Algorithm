import sys

def main(n, m):
    dist = list(map(int, input().split()))
    left, right = [], []
    max_value = -1
    for d in dist:
        if d > 0:
            right.append(d)
        
        else:
            left.append(-d)
        
        max_value = max(max_value, abs(d))
        
    right.sort(reverse=True)
    left.sort(reverse=True)
    
    total = 0
    # right
    for i in range(0, len(right), m):
        if right[i] != max_value:
            total += (right[i] * 2)
        
    # left
    for i in range(0, len(left), m):
        if left[i] != max_value:
            total += (left[i] * 2)
            
    return total + max_value


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    print(main(n, m))
    