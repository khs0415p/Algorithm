import sys

def main(k):
    
    numbers = [input().rstrip() for _ in range(k)]
    numbers.sort()
    for a, b in zip(numbers[:-1],numbers[1:]):
        if b.startswith(a):
            return "NO"
        
        
        
    return 'YES'

    



if __name__ == "__main__":
    input = sys.stdin.readline
    k = int(input())
    for _ in range(k):
        print(main(int(input())))