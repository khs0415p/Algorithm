import sys

def main(n, dir):
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    answer = 0
    def dfs(x, y, depth, visited, p):
        nonlocal answer
        
        if depth == n:
            answer += p
            return
        
        for i in range(4):
            if dir[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dfs(nx, ny, depth+1, visited, p * dir[i])
                    visited.remove((nx, ny))
                
    dfs(0, 0, 0, set([(0,0)]), 1)
    
    
    return answer
    

if __name__ == "__main__":
    input = sys.stdin.readline
    
    num, e, w, s, n = map(int, input().split())
    dir = [e/100, w/100, s/100, n/100]
    print(main(num, dir))
     