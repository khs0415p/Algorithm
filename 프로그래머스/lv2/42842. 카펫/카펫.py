def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(total, int(total ** 0.5)-1, -1):
        if not total % i:
            h_hat = total // i
            if 2*h_hat + 2 * (i-2) == brown:
                return [i, h_hat]
            