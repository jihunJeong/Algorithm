import sys
from collections import deque

dirx = [0, 1, 0, -1]
diry = [1, 0, -1, 0]

# 시간이 200초 이므로 [400][400][200] 으로 만들어서 해결
dp = [[[0 for z in range(201)] for x in range(401)] for y in range(401)]
a = [[[0 for z in range(201)] for x in range(401)] for y in range(401)]

xs, ys = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
xh, yh = map(int, sys.stdin.readline().split())
dx, dy = xh + (200 - xs), yh + (200 - ys)

n = int(sys.stdin.readline())
for i in range(n):
	a, b = map(int, sys.stdin.readline().split())
	if abs(a - xs) > 200 or abs(b - ys) > 200:
		continue
	dp[b-ys+200][a-xs+200][0] = -1

if abs(xh - xs) + abs(yh - ys) > t:
	print(0)
else :
	time = 0
	poss = deque([[200, 200, 0]])
	while poss:
		y, x, l = poss.popleft()
		if l >= t:
			break
		for i in range(4):
			nx = x + dirx[i]
			ny = y + diry[i]

			if dp[ny][nx][0] != -1 and abs(nx - dx) + abs(ny - dy) <= t - l: 
				dp[ny][nx][l+1] += 1
				poss.append([ny, nx, l+1])

	print(sum(dp[dy][dx]) % 1000000007)
