import sys
input = sys.stdin.readline


def main(N):
    def adjs(r, c):
        if 0 < r:  yield r-1, c
        if 0 < c:  yield r, c-1
        if r < N-1:  yield r+1, c
        if c < N-1:  yield r, c+1


    board = [list(map(int, input().split())) for _ in range(N)]
    island_id = -1
    edges = []
    for r in range(N):
        for c in range(N):
            if board[r][c] <= 0:
                continue
            board[r][c] = island_id
            stack = [(r, c)]
            tmp = set()
            while stack:
                r, c = stack.pop()
                for rr, cc in adjs(r, c):
                    if board[rr][cc] <= 0:
                        if not board[rr][cc]:
                            tmp.add((r, c))
                        continue
                    board[rr][cc] = island_id
                    stack.append((rr, cc))
            island_id -= 1
            edges.append(list(tmp))

    bridge = 10000
    for i in range(len(edges)):
        is_visited = [[False] * N for _ in range(N)]
        que = edges[i]
        dist = 0
        while dist < bridge:
            tmp = []
            for r, c in que:
                for rr, cc in adjs(r, c):
                    if board[rr][cc] == ~i or is_visited[rr][cc]:
                        continue
                    if board[rr][cc] < 0:
                        bridge = dist
                    is_visited[rr][cc] = True
                    tmp.append((rr, cc))
            que = tmp
            dist += 1
    return bridge


if __name__ == '__main__':
    answer = main(int(input()))
    print(answer)