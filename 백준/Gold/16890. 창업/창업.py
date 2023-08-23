import sys
from collections import deque


def main(apple, cube):
    length = len(apple)
    
    apple = deque(sorted(apple)[:(length+1)//2])
    cube = deque(sorted(cube, reverse=True)[:(length//2)])
    answer = [0] * length
    
    left, right = 0, length-1
    for i in range(length):
        if i % 2:
            # 큐브에서 제일 큰 값이, 애플의 제일 작은값보다 작거나 같음 -> 큐브는 제일 작은 값을 뒤에다 배치
            if apple and cube[0] <= apple[0]:
                answer[right] = cube.pop()
                right -= 1
            
            # 큐브에서 제일 큰 값이, 애플의 제일 작은값보다 큼 -> 큐브는 제일 큰 값을 앞에다 배치
            else:
                answer[left] = cube.popleft()
                left += 1
            
        else:
            # 애플은 제일 작은 값이, 큐브의 제일 큰값 보다 큼 -> 애플의 젤 큰 값을 맨뒤로 배치
            if cube and apple[0] >= cube[0]:
                answer[right] = apple.pop()
                right -= 1
                
            # 애플의 제일 작은 값이, 큐브의 제일 큰값보다 작음 -> 작은값을 앞쪽에 배치
            else:
                answer[left] = apple.popleft()
                left += 1
    
    
    return ''.join(answer)
    

if __name__ == "__main__":
    input = sys.stdin.readline
    apple, cube = input().rstrip(), input().rstrip()
    print(main(apple, cube))