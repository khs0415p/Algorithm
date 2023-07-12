import sys
input = sys.stdin.readline

def main(board):
    
    # check List
    row_check = [[False] * 10 for _ in range(9)]
    col_check = [[False] * 10 for _ in range(9)]
    bnd_check = [[False] * 10 for _ in range(9)]
    emptys = []
    for i in range(9):
        for j in range(9):
            if board[i][j]:
                cur = board[i][j]
                row_check[i][cur] = True
                col_check[j][cur] = True
                bnd_check[(i//3)*3 + j//3][cur] = True
            else:
                emptys.append((i, j))
                
    
    def backTrack(i):
        if i == len(emptys):
            return True
        
        r, c = emptys[i]
        for num in range(1, 10):
            if not row_check[r][num] and not col_check[c][num] and not bnd_check[(r//3) * 3 + (c//3)][num]:
                board[r][c] = num
                row_check[r][num] = col_check[c][num] = bnd_check[(r//3)*3 + (c//3)][num] = True
                if backTrack(i+1):
                    return True
                board[r][c] = 0
                row_check[r][num] = col_check[c][num] = bnd_check[(r//3)*3 + (c//3)][num] = False
    
    backTrack(0)
    
    for b in board:
        print(*b)

if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(9)]
    main(board)