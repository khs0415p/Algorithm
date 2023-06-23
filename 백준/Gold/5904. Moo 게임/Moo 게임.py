import sys
sys.setrecursionlimit(10**6)

def main(k):
    
    def recur(word_len, n, k):
        prev = (word_len - (n + 3)) // 2
        
        # 앞
        if prev >= k:
            # print("앞에 있음")
            return recur(prev, n-1, k)
            
        # 끝
        elif prev + (n+3) < k:
            # print("뒤에 있음")
            return recur(prev, n-1, k - prev - (n+3))
            
        # 중간에 있음
        else:
            # 처음만 아니면 o
            
            return "m" if k-prev == 1 else "o"
    
    n = 0
    word_len = 3
    while word_len < k:
        n += 1
        word_len = word_len * 2 + n + 3 
        
        
    
    return recur(word_len, n, k)
    



if __name__ == "__main__":
    input = sys.stdin.readline
    k = int(input())
    print(main(k))