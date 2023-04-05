def solution(sequence):
    n = len(sequence)
    psum = [0] * (n+1)
    p = 1
    for i in range(n):
        psum[i+1] = psum[i] + sequence[i]*p;
        p *= -1
    
    return max(psum) - min(psum)