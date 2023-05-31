import sys

def main(text, exp):
    
    new_text = []
    for t in text:
        if len(new_text) < len(exp) - 1:
            new_text.append(t)
            continue
        
        if len(exp) == 1:
            if t != exp:
                new_text.append(t)
            continue
            
        else:
            check = ''.join(new_text[-(len(exp)-1):]) + t
            
        if check == exp:
            cnt = 0
            while cnt < len(exp)-1:
                new_text.pop()
                cnt += 1
        else:
            new_text.append(t)
            
    return ''.join(new_text) if new_text else "FRULA"
        


if __name__ == "__main__":
    input = sys.stdin.readline
    text = input().rstrip()
    exp = input().rstrip()
    print(main(text, exp))