import sys

def main():
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))
    
    def post_order(root, start, end):
        
        if start >= end:
            return
        
        for i in range(start, end):
            if pre_order[root] == in_order[i]:
                post_order(root + 1, start, i)
                post_order(root + 1 + (i - start), i + 1, end)
                print(pre_order[root], end = " ")

    post_order(0, 0, len(pre_order))
    
if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        main()
        print()