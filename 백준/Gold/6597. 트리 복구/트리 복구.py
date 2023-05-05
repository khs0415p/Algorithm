import sys


def main(pre_order, in_order):
    """_summary_

    in_order는 중심을 기준으로 왼쪽 트리 / 오른쪽 트리를 알 수 있음
    pre_order는 나누어진 트리에서 root가 누구인지 알 수 있음
    자식 트리의 루트를 기준으로 in_oder의 왼쪽, 오른쪽의 여부에 따라 트리를 그릴 수 있음
    """
    # r - L - R / L - r - R  -> L - R - r
    def post_order(root, start, end):
        if start > end:
            return
        
        for i in range(start, end):
            if pre_order[root] == in_order[i]:
                post_order(root+1, start, i)
                post_order(root+1+(i-start), i+1, end)
                print(pre_order[root], end='')
                
    post_order(0, 0, len(pre_order))

if __name__ == "__main__":
    input = sys.stdin.readline
    
    
    try:
        while True:
            pre_order, in_order = input().rstrip().split()
            main(pre_order, in_order)
            print()
            
    except:
        pass
    