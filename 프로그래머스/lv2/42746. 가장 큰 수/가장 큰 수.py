def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = lambda x:(x*4)[:4], reverse=True)
    result = ''.join(numbers)
    
    return "0" if result[0] == "0" else result