import sys

def main(n, k, number):
    
    stack = []
    target_length = n - k
    for i in range(len(number)):
        while stack and stack[-1] < number[i] and k > 0:
            stack.pop()
            k -= 1
        stack.append(number[i])
    print(''.join(stack[:target_length]))
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    number = input()
    main(n, k, number)