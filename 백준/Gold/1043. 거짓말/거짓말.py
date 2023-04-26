import sys

def main(n, m, know_set):
    
    if not know_set: return m
    
    graph = {i:set() for i in range(1, n+1)}
    parties = []
    
    for _ in range(m):
        party = set(map(int, input().split()[1:]))
        parties.append(party)
        for p in party:
            graph[p].update(party - set([p]))
            
    answer = 0
    # print(graph)
    for party in parties:
        flag = False
        for per in party:
            stack = [per]
            visited = set([per])
            while stack:
                cur_node = stack.pop()
                
                if cur_node in know_set:
                    flag = True
                    break
                
                for node in graph[cur_node]:
                    if node not in visited:
                        visited.add(node)
                        stack.append(node)
        if not flag:
            answer += 1
                
                    
    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    # 사람수 / 파티수
    n, m = map(int, input().split())
    # 알고있는 사람 수 / 번호
    know_set = set(map(int, input().split()[1:]))
    
    print(main(n, m, know_set))