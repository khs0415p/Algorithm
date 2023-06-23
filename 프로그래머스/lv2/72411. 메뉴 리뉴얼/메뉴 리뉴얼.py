from itertools import combinations
from collections import Counter

def solution(orders, course):
    
    answer = []
    for c in course:
        check_dic = Counter()
        for order in orders:
            for combi in combinations(sorted(order), c):
                check_dic.update([combi])
                
        if not check_dic: break
        
        check_dic = sorted(check_dic.items(), key=lambda x:-x[1])
        pivot = check_dic[0][1]
        if pivot < 2: continue
        for k, v in check_dic:
            if pivot != v: break
            answer.append(''.join(k))
            
    return sorted(answer)