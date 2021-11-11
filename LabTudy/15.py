from collections import defaultdict
from collections import deque

N, M, K, X = map(int, input().split())
graph = defaultdict(list)

for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

visited = [0] * (N+1)
dq = deque([[X, 0]])
visited[X] = 1
answer = []
while dq:
    node, cost = dq.popleft()
    if cost == K:
        answer.append(node)
    
    for n in graph[node]:
        if visited[n] == 1:
            continue
        dq.append([n, cost+1])
        visited[n] = 1

if not answer:
    print(-1)
for n in sorted(answer):
    print(n)
