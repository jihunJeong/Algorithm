from collections import defaultdict
from itertools import combinations
import copy

def make_dict(sub, score, dfd):
    dfd[''.join(s for s in sub)].append(score)
    c = [0, 1, 2, 3]
    for i in range(1, 5):
        cb = list(combinations(c, i))
        for j in cb:
            temp = copy.deepcopy(sub)
            for k in j:
                temp[k] = "-"
            dfd[''.join(s for s in temp)].append(score)
            
def solution(info, query):
    answer = []
    dfd = defaultdict(list)
    for i in info:
        sub = list(i.split())
        make_dict(sub[:4], int(sub[4]), dfd)
    
    for k in dfd.keys():
        dfd[k] = sorted(dfd[k])
        
    for q in query:
        sub = []
        temp = list(q.split())
        for t in temp:
            if t != "and":
                sub.append(t)
        arr = dfd[''.join(sub[s] for s in range(4))]
        target = int(sub[4])
        s, e, ans_id = 0, len(arr)-1, 10000000
        while s <= e:
            mid = (s+e) // 2
            if arr[mid] >= target:
                e = mid - 1
                ans_id = min(ans_id, mid)
            else :
                s = mid + 1
        cnt = len(arr) - ans_id
        if cnt < 0:
            cnt = 0
        answer.append(cnt)
    return answer