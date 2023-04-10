import heapq

def calculate_dist(pos, target):
    t_x, t_y = abs(pos[0] - target[0]), abs(pos[1] - target[1])
    
    return max(1, min(t_x, t_y) * 3 + (max(t_x, t_y) - min(t_x, t_y)) * 2)

def solution(number):
    phones = {num : divmod(int(num)-1, 3) for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']}
    queue = [[0, '4', '6']]
    for num in number:
        if num == "0":
            num = '11'
            
        temp = []
        visited = set()
        while queue:
            weight, left, right = heapq.heappop(queue)
            if left == right: continue
            
            left_pos, right_pos = phones[left], phones[right]
            if (left_pos[0], left_pos[1], right_pos[0], right_pos[1]) in visited: continue
            visited.add((left_pos[0], left_pos[1], right_pos[0], right_pos[1]))
            heapq.heappush(temp, [weight + calculate_dist(left_pos, phones[num])] + [num, right])
            heapq.heappush(temp, [weight + calculate_dist(right_pos, phones[num])] + [left, num])
        queue = temp
        
    
    return queue[0][0]

solution('5123')