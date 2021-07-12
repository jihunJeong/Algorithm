import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

t = int(sys.stdin.readline())
for _ in range(t):	
	ans = 0
	m, n, k = map(int, sys.stdin.readline().split())
	b = [[0 for _ in range(m)] for _ in range(n)]

	for _ in range(k):
		x, y = map(int, input().split())
		b[y][x] = 1
	
	s = []

	for i in range(n):
		for j in range(m):
			if b[i][j] == 0:
				continue
			ans += 1
			s.append([i,j])
			while s:
				y, x = s.pop()
				b[y][x] = 0
				
				for k in range(4):
					ny, nx = y+dy[k], x+dx[k]
					if ny < 0 or nx < 0 or ny >= n or nx >= m:
						continue

					if b[ny][nx] == 1:
						s.append([ny, nx])
	
	print(ans)