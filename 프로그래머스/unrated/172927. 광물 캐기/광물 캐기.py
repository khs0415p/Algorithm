def solution(picks, minerals):
    answer = 0
    ntoi = {"diamond":0, "iron":1, "stone":2}
    ntov = {"diamond":25, "iron":5, "stone":1}
    iton = {0:"diamond", 1:"iron", 2:"stone"}
    table = {"diamond": {"dia": 1, "iron": 1, "stone": 1},
            "iron": {"dia": 5, "iron": 1, "stone": 1},
            "stone": {"dia": 25, "iron": 5, "stone": 1}
            }
    
    check = []
    
    num_min = sum(picks) * 5
    if len(minerals) > num_min:
        minerals = minerals[:num_min]
        
    for i in range(0, len(minerals), 5):
        tmp = [0, 0, 0]
        for m in minerals[i: i+5]:
            tmp[ntoi[m]] += ntov[m]
        check.append(tmp)
    check.sort(key = lambda x:sum(x))
    
    answer = 0
    for i in range(3):
        if not picks[i]: continue
        
        name = iton[i]
        for _ in range(picks[i]):
            if not check: break
            d, s, ss = check.pop()
            answer += table[name]["dia"] * d//25
            answer += table[name]["iron"] * s//5
            answer += table[name]["stone"] * ss//1
    return answer