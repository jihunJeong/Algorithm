from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    for n in course:
        info = defaultdict(int)
        for o in orders:
            rst = list(combinations(o, n))
            for r in rst:
                info[''.join(s for s in sorted(list(r)))] += 1
        count = 2
        candidates = []
        for key in info.keys():
            if info[key] == count:
                candidates.append(key)
            elif info[key] > count:
                count = info[key]
                candidates =[key]
        answer.extend(candidates)
    answer = sorted(answer)    
    return answer