import sys

def make_table(text):
     
    table = [0] * len(text)
    
    i = 0
    # ababc
    for j in range(1, len(text)):
        while i > 0 and text[i] != text[j]:
            i = table[i-1]
        
        if text[i] == text[j]:
            i += 1
            table[j] = i
            
    return max(table)

def main(text):
    
    result = 0
    for i in range(len(text)):
        result = max(result, make_table(text[i:]))
    return result
        


if __name__ == "__main__":
    input = sys.stdin.readline
    text = input().rstrip()
    print(main(text))
    