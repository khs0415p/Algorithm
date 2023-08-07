from collections import deque

def solution(n, t, m, timetable):
    
    for i in range(len(timetable)):
        h, mi = timetable[i].split(":")
        timetable[i] = int(h) * 60 + int(mi)
    timetable.sort()
    timetable = deque(timetable)
    cur_time = 9 * 60
    end_time = cur_time + (n-1) * t
    answer = 0
    idx = 0
    while cur_time <= end_time:
        cur_m = m
        stack = []
        
        while 0 <= idx < len(timetable) and cur_m:
            if timetable[idx] <= cur_time:
                stack.append(timetable[idx])
                cur_m -= 1
            else:
                break
            idx += 1
        if cur_m:
            answer = cur_time
        else:
            answer = stack[-1] - 1
            
        cur_time += t
    hour, min = divmod(answer, 60)
    return ''.join([str(hour).rjust(2, '0'), ":",str(min).rjust(2, '0')])