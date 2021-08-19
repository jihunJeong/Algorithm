from collections import deque, defaultdict

N = int(input())
s, e = map(int, input().split())
m = int(input())

graph = defaultdict(list)
for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dq = deque([[s, 0]])
visited = [False for _ in range(N+1)]
visited[s], flag = True, False
while dq:
    node, c = dq.popleft()

    if node == e:
        print(c)
        flag = True
        break

    for n in graph[node]:
        if not visited[n]:
            dq.append([n,c+1])
            visited[n] = True

if not flag:
    print(-1)