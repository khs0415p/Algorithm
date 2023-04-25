# 상하반전
# 좌우반적
# 오른쪽 90도
# 왼쪽 90도
# 5, 6번 연산을 수행하려면 배열을 크기가 N/2×M/2인 4개의 부분 배열로 나눠야 한다. 아래 그림은 크기가 6×8인 배열을 4개의 그룹으로 나눈 것이고, 1부터 4까지의 수로 나타냈다.
# 5번 연산은 1번 그룹의 부분 배열을 2번 그룹 위치로, 2번을 3번으로, 3번을 4번으로, 4번을 1번으로 이동시키는 연산이다.
# 6번 연산은 1번 그룹의 부분 배열을 4번 그룹 위치로, 4번을 3번으로, 3번을 2번으로, 2번을 1번으로 이동시키는 연산이다.
import sys

def up_down(board):
    n, m = len(board), len(board[0])
    new_board = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_board[n-i-1][j] = board[i][j]
            
    return new_board

def left_right(board):
    n, m = len(board), len(board[0])
    new_board = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_board[i][m-j-1] = board[i][j]
            
    return new_board

def rotation(board, isLeft=False):
    n, m = len(board), len(board[0])
    new_board = [[0] * n for _ in range(m)]
    
    if isLeft:
        
        for i in range(n):
            for j in range(m):
                new_board[m-j-1][i] = board[i][j]
        
    else:
        for i in range(n):
            for j in range(m):
                new_board[j][n-i-1] = board[i][j]
            
    return new_board

def transfer(board, isReverse=False):
    n, m = len(board), len(board[0])
    new_board = [[0] * m for _ in range(n)]
    row_half, col_half = n//2, m//2
    
    if isReverse:
        for i in range(n):
            for j in range(m):
                if 0 <= i < row_half and 0 <= j < col_half:
                    new_board[i+row_half][j]= board[i][j]
                    
                elif 0 <= i < row_half and col_half <= j < m:
                    new_board[i][j-col_half] = board[i][j]
                    
                elif row_half <= i < n and col_half <= j < m:
                    new_board[i-row_half][j] = board[i][j]
                    
                else:
                    new_board[i][j+col_half] = board[i][j]
        
    else:
        
        
        
        for i in range(n):
            for j in range(m):
                if 0 <= i < row_half and 0 <= j < col_half:
                    new_board[i][j+col_half]= board[i][j]
                    
                elif 0 <= i < row_half and col_half <= j < m:
                    new_board[i+(n//2)][j] = board[i][j]
                    
                elif row_half <= i < n and col_half <= j < m:
                    new_board[i][j-col_half] = board[i][j]
                    
                else:
                    new_board[i-row_half][j] = board[i][j]
                    
    return new_board

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, op = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    opers = list(map(int, input().split()))
    
    for oper in opers:
        if oper == 1:
            board = up_down(board)
            
        elif oper == 2:
            board = left_right(board)
            
        elif oper == 3:
            board = rotation(board)
            
        elif oper == 4:
            board = rotation(board, True)
            
        elif oper == 5:
            board = transfer(board)
            
        else:
            board = transfer(board, True)
            
    for b in board:
        print(*b)
        