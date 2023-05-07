def check_palin(string):
    return string == string[::-1]

def solution(s):
    answer = 0
    length = len(s)
    max_v = -1
    for i in range(length):
        for j in range(i,length+1):
            # print(s[i:j])
            if check_palin(s[i:j]):
                if max_v < len(s[i:j]):
                    max_v = len(s[i:j])
    return max_v