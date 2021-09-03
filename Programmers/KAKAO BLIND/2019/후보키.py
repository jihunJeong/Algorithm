from itertools import combinations
from collections import defaultdict
def unique(relation, cb):
    info = []
    for r in relation:
        temp = []
        for c in cb:
            temp.append(r[c])
        info.append(temp)
        
    cnt = defaultdict(int)
    for i in info:
        if cnt[''.join(s for s in i)] > 0:
            return False
        else :
            cnt[''.join(s for s in i)] += 1
    return True
    
def solution(relation):
    answer = 0
    column = len(relation[0])
    index = [x for x in range(column)]
    
    ans = []
    for i in range(1, column+1):
        comb = list(combinations(index, i))
        for cb in comb:
            flag = 0
            for j in range(1, len(cb)):
                ch = list(combinations(cb, j))
                for c in ch:
                    if c in ans:
                        flag = 1
            if not flag and unique(relation, cb):
                answer += 1
                ans.append(cb)
    return answer