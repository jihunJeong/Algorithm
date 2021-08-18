from itertools import combinations, permutations

N, M = map(int, input().split())
li = [x for x in range(1, N+1)]
p = combinations(li, M)
for a in p:
    print(" ".join(str(e) for e in a))