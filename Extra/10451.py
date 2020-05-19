import sys

T = int(sys.stdin.readline())
for i in range(T):
	N = int(sys.stdin.readline())
	visited = [0 for x in range(N)]

	num = list(map(int, input().split()))
	ans = 0
	start = 0
	count = 0
	while(True):
		if visited[start] == 1:
			ans += 1
			if count == N:
				break
			else :
				start = visited.index(0)
				continue

		visited[start] = 1
		count += 1
		start = num[start] - 1

	print(ans)