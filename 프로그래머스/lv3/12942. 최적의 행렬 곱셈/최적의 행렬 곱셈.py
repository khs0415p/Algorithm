def solution(matrix_sizes):
    mat_len = len(matrix_sizes)
    dp = [[float("inf")] * mat_len for _ in range(mat_len)]
    
    # 자기 자신 초기화
    for i in range(mat_len):
        dp[i][i] = 0
    
    # ABCE -> A BCE -> AB CE -> ABC E
    for i in range(1, mat_len):
        for j in range(mat_len - i):
            start = j
            end = j + i
            for k in range(start, end):
                dp[start][end] = min(dp[start][end],
                                     dp[start][k] + dp[k + 1][end] + matrix_sizes[start][0] * matrix_sizes[k][1] * matrix_sizes[end][1])
                
    return dp[0][mat_len - 1]