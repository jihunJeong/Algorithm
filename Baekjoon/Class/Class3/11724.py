from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

ans = 0
check = [0]*(N+1)
for i in range(1,N+1):
    if check[i] == 1:
        continue
    ans += 1
    s = [i]
    while s:
        nn = s.pop()
        if check[nn] == 1:
            continue
        check[nn] = 1
        s.extend(graph[nn])

print(ans)