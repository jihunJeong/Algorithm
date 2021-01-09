import sys
from collections import deque

n = int(sys.stdin.readline())
cnt = int(sys.stdin.readline())

virus = [0] * (n+1)
virus[1] = 1
graph = [[] for _ in range(n+1)]

for i in range(cnt):
	a, b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)

q = deque([1])
while q:
	s = q.popleft()

	for i in graph[s]:
		if virus[i] == 1:
			continue
		q.append(i)
		virus[i] = 1

print(sum(virus)-1)