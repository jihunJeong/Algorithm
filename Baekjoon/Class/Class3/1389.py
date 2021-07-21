import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
graph = [[10000000 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    graph[i][i] = 0

for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

for k in range(1,N+1):
    for s in range(1,N+1):
        for e in range(1,N+1):
            if graph[s][e] > graph[s][k]+graph[k][e]:
                graph[s][e] = graph[s][k]+graph[k][e]

ans_p, ans_m = 0, 100000000
for i in range(1,N+1):
    s = sum(graph[i])

    if s < ans_m :
        ans_p = i
        ans_m = s
print(ans_p)