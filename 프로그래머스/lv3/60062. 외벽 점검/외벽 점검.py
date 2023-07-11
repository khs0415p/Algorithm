def solution(n, weak, dist):
    dist.sort(reverse=True)
    r_list = [()]
    count = 0
    for d in dist:
        repairs = []
        count += 1
        for i, w in enumerate(weak):
            start = w
            ends = weak[i:] + [w+n for w in weak[:i]]
            can_ends = [end%n for end in ends if (end - start) <= d]
            repairs.append(set(can_ends))
        
        cand = set()
        for r in repairs:
            for l in r_list:
                new = r | set(l)
                if len(new) == len(weak):
                    return count
                cand.add(tuple(new))
        r_list = cand
        
    return -1