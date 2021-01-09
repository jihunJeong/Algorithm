import sys

t = int(sys.stdin.readline())
while t:
	t -= 1	
	m, n, k = map(int, sys.stdin.readline().split())
	board = [[[0, 0] for x in range(m)] for y in range(n)]
	cnt = 0
	for i in range(k):
		x, y = map(int, sys.stdin.readline().split())
		board[y][x][0] = 1

	for i in range(n):
		for j in range(m):
			if board[i][j][0] == 1 and board[i][j][1] == 0: