def solution(plans):
    
    length = len(plans)
    for i in range(length):
        plan = plans[i]
        h, m = map(int, plan[1].split(":"))
        h = h * 60
        plan[1] = h + m
        plan[2] = int(plan[-1])
    plans.sort(key=lambda x:x[1])
    
    ready = []
    answer = []
    cur_time = plans[0][1]
    for i in range(length):
        while ready and cur_time < plans[i][1]:
            plan = ready.pop()
            if cur_time + plan[2] <= plans[i][1]:
                cur_time += plan[2]
                answer.append(plan[0])
                
            else:
                plan[2] -= (plans[i][1] - cur_time)
                cur_time = plans[i][1]
                ready.append(plan)
            
        cur_time = plans[i][1]
        ready.append(plans[i])
            
    while ready:
        answer.append(ready.pop()[0])
    
    return answer