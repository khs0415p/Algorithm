def solution(answers):
    
    f_s = '12345'
    s_s = '21232425'
    t_s = '3311224455'
    
    length = len(answers)
    f_a = f_s * (length//len(f_s)) + f_s[:length%len(f_s)]
    s_a = s_s * (length//len(s_s)) + s_s[:length%len(s_s)]
    t_a = t_s * (length//len(t_s)) + t_s[:length%len(t_s)]
    
    corrected = [0,0,0]
    for a, f, s, t in zip(answers, f_a, s_a, t_a):
        corrected[0] += (int(f) == a)
        corrected[1] += (int(s) == a)
        corrected[2] += (int(t) == a)
        
    results = []
    max_value = max(corrected)
    for i in range(3):
        if max_value == corrected[i]:
            results.append(i+1)
        
    return results