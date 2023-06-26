def solution(rows, columns, queries):
    
    def rotation(x1, y1, x2, y2):
        x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
        
        temp = board[x1][y1]
        min_value = temp
        
        #좌
        for r in range(x1, x2):
            board[r][y1] = board[r+1][y1] 
            min_value = min(min_value, board[r+1][y1])
        #하
        for c in range(y1, y2):
            board[x2][c] = board[x2][c+1]
            min_value = min(min_value, board[x2][c+1])
        #우 
        for r in range(x2, x1, -1):
            board[r][y2] = board[r-1][y2]
            min_value = min(min_value, board[r-1][y2])
        #상
        for c in range(y2, y1, -1):
            board[x1][c] = board[x1][c-1]
            min_value = min(min_value, board[x1][c-1])
        board[x1][y1 + 1] = temp
        return min_value
    
    board = [[(columns*j) + i for i in range(1, columns+1)] for j in range(rows)]
    answer = []
    for query in queries:
        x1, y1, x2, y2 = query
        answer.append(rotation(x1, y1, x2, y2)) 
                    
    return answer

# 8 10 25
solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])