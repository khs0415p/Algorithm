def solution(s):
    length = len(s)
    answer = []
    for size in range(1, length//2+1):
        result = ''
        count = 1
        tmp = s[:size]
        for i in range(size, length, size):
            if tmp == s[i:i+size]:
                count += 1
            else:
                if count > 1:
                    result = result + str(count) + tmp
                else:
                    result = result + tmp
                count = 1
                tmp = s[i:i+size]
                
        if count > 1:
            result = result + str(count) + tmp
        else:
            result = result + tmp
        answer.append(len(result))
    return min(answer) if answer else 1