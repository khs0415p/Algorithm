import sys
sys.setrecursionlimit(100000)

# 로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.
def main(n, m):

    s_r, s_c, s_d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    count = 1
    room[s_r][s_c] = -1
    
    def dfs(x, y, dir, flag):
        nonlocal count
        for _ in range(4):
            dir = (dir - 1) % 4
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 > nx or 0 > ny or n <= nx or m <= ny or room[nx][ny] == 1 or room[nx][ny] == -1:
                continue
            room[nx][ny] = -1
            count += 1
            dfs(nx, ny, dir, False)
            flag = True
            break
                
        if not flag:
            nx, ny = x - dx[dir], y - dy[dir]
            if room[nx][ny] == 1:
                return
            else:
                dfs(nx, ny, dir, False)
            
        return
    
    dfs(s_r, s_c, s_d, False)
    return count
    

if __name__ == "__main__":
    input = sys.stdin.readline
    # 3 <= n,m <= 50
    n, m = map(int, input().split())
    print(main(n, m))
    