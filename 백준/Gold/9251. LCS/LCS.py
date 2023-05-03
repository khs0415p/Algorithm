import sys

def main(sentence_one, sentence_two):
    n, m  = len(sentence_one), len(sentence_two)
    matrix = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            
            flag = sentence_one[i-1] == sentence_two[j-1]
            if flag:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    
    return matrix[-1][-1]

if __name__ == "__main__":
    input = sys.stdin.readline
    sentence_one = input().strip()
    sentence_two = input().strip()
    
    print(main(sentence_one, sentence_two))
    