import sys
input = sys.stdin.readline


if __name__ == '__main__':
    string = input().rstrip()
    bomb = input().rstrip()
    lb, ls = len(bomb), len(string)
    stack = []
    cur = []
    
    si = 0
    i = 0
    while si < ls:
        if i == lb:
            del cur[-lb:]
            i = stack.pop() if stack else 0
            continue
        if string[si] == bomb[i]:
            i += 1
        else:
            if i and string[si] == bomb[0]:
                stack.append(i)
                i = 1
            else:
                stack = []
                i = 0
        cur.append(string[si])
        si += 1
    
    if i == lb:
        del cur[-lb:]
    print(''.join(map(str, cur)) if cur else 'FRULA')