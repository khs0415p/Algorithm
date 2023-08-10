import sys
from collections import deque


def main(n, m):
    
    moves = {}
    for _ in range(n+m):
        s, e = map(int, input().split())
        moves[s] = e
    
    dices = [1, 2, 3, 4, 5, 6]
    queue = deque([[1, 0]])
    visited = [0] * 101
    visited[1] = 1
    if 1 in moves:
        queue.append([moves[1], 0])
    
    while queue:
        cur_pos, cur_cnt = queue.popleft()
        if cur_pos == 100:
            return cur_cnt
        
        for dice in dices:
            n_pos = cur_pos + dice
            if 1 > n_pos or 100 < n_pos or visited[n_pos]: continue
            
            visited[n_pos] = 1

            if n_pos in moves:
                visited[moves[n_pos]] = 1
                queue.append([moves[n_pos], cur_cnt + 1])
            else:
                queue.append([n_pos, cur_cnt + 1])
            

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    print(main(n, m))