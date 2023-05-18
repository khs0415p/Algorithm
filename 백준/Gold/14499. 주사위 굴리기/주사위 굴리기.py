import sys

def main(n, m, s_x, s_y, c):
    """
    바닥 윗면 왼쪽 오른쪽 위 아래
    6   1   4   3    5  2
    
    아래로 굴리기
    
    2  5   4   3    6  1
    
    위로 굴리기
    
    5  2  4   3    1  6
    
    왼쪽 굴리기
    
    4  3   1   6  5  2
    
    오른쪽 굴리기
    3  4   6   1  5  2
    
    """
    
    direct = {"1": (0, 1), "2": (0, -1), "3": (-1, 0), "4": (1, 0)}
    board = [list(map(int, input().split())) for _ in range(n)]
    dice = [6, 1, 4, 3, 5, 2]
    dice_map = [0] * 7
    for op in input().split():
        dx, dy = direct[op]
        nx = dx + s_x
        ny = dy + s_y
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        s_x = nx
        s_y = ny
        
        if op == '1':
            dice = [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]
            
        elif op == "2":
            dice = [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]
            
        elif op == "3":
            dice = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
            
        else:
            dice = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]
        
        
        if board[s_x][s_y]:
            dice_map[dice[0]] = board[s_x][s_y]
            board[s_x][s_y] = 0
            
            
        else:
            board[s_x][s_y] = dice_map[dice[0]]
            
        print(dice_map[dice[1]])
    

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, s_x, s_y, c = map(int, input().split())
    main(n, m, s_x, s_y, c)