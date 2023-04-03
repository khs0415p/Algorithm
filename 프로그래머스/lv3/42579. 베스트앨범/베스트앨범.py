
# def solution(genres, plays):
#     answer = []
#     d = {e:[] for e in set(genres)}
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1] , e[2]])
#     genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
#         answer += temp[:min(len(temp),2)]
#     return answer

from collections import defaultdict

def solution(genres, plays):
    
    genre_to_plays = defaultdict(int)
    genre_to_song = defaultdict(list)
    for i, (g,p) in enumerate(zip(genres, plays)):
        genre_to_plays[g] += p
        genre_to_song[g].append([i, p])
        
    answer = []
    for k, _ in sorted(genre_to_plays.items(), key=lambda x:-x[-1]):
        answer.extend(sorted(genre_to_song[k], key=lambda x:[-x[-1], x[0]])[:2])
    
    return [i for i, _ in answer]