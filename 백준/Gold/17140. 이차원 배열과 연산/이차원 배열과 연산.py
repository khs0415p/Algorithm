from itertools import chain
import sys

def main(r, c, k):
    matrix = [list(map(int, input().split())) for _ in range(3)]
    
    for time in range(101):
        
        if r < len(matrix) and c < len(matrix[0]) and matrix[r][c] == k:
            return time
        
        if len(matrix) >= len(matrix[0]):
            
            max_col = 0
            for i in range(len(matrix)):
                
                counter = {}
                for ele in matrix[i]:
                    if not ele: continue
                    counter[ele] = counter.get(ele, 0) + 1
                
                # 빈도수 -> 숫자
                # [[1, 3], [2, 4]]
                matrix[i] = list(chain(*sorted([[k, v] for k, v in counter.items()], key=lambda x:[x[1], x[0]])))[:100]
                max_col = max(max_col, len(matrix[i]))
            
            
            # 0 삽입
            for i in range(len(matrix)):
                matrix[i] += [0] * (max_col - len(matrix[i]))
            
        else:
            
            
            for i in range(len(matrix[0])):
                counter = {}
                for j in range(len(matrix)):
                    ele = matrix[j][i]
                    if not ele: continue
                    counter[ele] = counter.get(ele, 0) + 1
                
                # 빈도수 -> 숫자
                # [[1, 3], [2, 4]]
                
                col = list(chain(*sorted([[k, v] for k, v in counter.items()], key=lambda x:[x[1], x[0]])))[:100]
                plus_num = len(col) - len(matrix)
                
                for _ in range(plus_num):
                    matrix.append([0] * len(matrix[0]))
                    
                for j in range(len(matrix)):
                    if j >= len(col):
                        matrix[j][i] = 0
                        
                    else:
                        matrix[j][i] = col[j]
                
    return -1
        
        
        
    

if __name__ == "__main__":
    input = sys.stdin.readline
    
    r,c,k = map(int, input().split())
    r, c = r - 1, c - 1
    print(main(r, c, k))
    