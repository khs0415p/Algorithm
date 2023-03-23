def solution(sizes):
    
    w, h = 0, 0
    for size in sizes:
        size.sort()
        w = max(w, size[-1])
        h = max(h, size[0])
        
    return w * h