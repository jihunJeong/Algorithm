from collections import defaultdict, deque

N = int(input())
graph = defaultdict(list)

for i in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

ans = {x:0 for x in range(1,N+1)}
dq = deque([1])
visited = [False for _ in range(N+1)]
visited[1] = True
while dq:
    node = dq.popleft()
    
    for n in graph[node]:
        if not visited[n]:
            dq.append(n)
            ans[n] = node
            visited[n] = True

for i in range(2, N+1):
    print(ans[i])