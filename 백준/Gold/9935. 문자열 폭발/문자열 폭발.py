import sys

def main(text, exp):
    
    new_text = []
    for t in text:
        new_text.append(t)
        if t == exp[-1] and ''.join(new_text[-(len(exp)):]) == exp:
            cnt = 0
            while cnt < len(exp):
                new_text.pop()
                cnt += 1
            
    return ''.join(new_text) if new_text else "FRULA"
        


if __name__ == "__main__":
    input = sys.stdin.readline
    text = input().rstrip()
    exp = input().rstrip()
    print(main(text, exp))