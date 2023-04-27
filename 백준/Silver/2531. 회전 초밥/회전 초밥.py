import sys
from collections import defaultdict

input = sys.stdin.readline

answer =0
n,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(n)]

l=0
r=0

dict = defaultdict(int)
dict[c] +=1

while r < k:
    dict[sushi[r]] +=1
    r+=1

while l < n:
    answer = max(answer, len(dict))
    dict[sushi[l]] -=1
    if dict[sushi[l]] == 0:
        del dict[sushi[l]]
    dict [sushi[r%n]] +=1
    l +=1
    r +=1

print(answer)