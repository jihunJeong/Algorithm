import sys

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
	queue = [y, x]
	while !queue.isempty():
		for i in range(4):
			cy, cx = queue.pop(0)

			ny = cy + dy[i]
			nx = cx + dx[i]
			if board[ny][nx] != 'x' and visit[ny][nx] == 0:
				visit[ny][nx] == 1
				queue.append([ny, nx])
				if board[ny][nx] == '*'

w, h = map(int, sys.stdin.readline().split())
board = [[0 for x in range(w)] for y in range(h)]
visit = [[0 for x in range(w)] for y in range(h)]

cx, cy = 0, 0
dust, funi = list(), list()
for i in range(h):
	input = list(sys.stdin.readline())
	for j in range(w):
		if input[j] == 'x':
			funi.append([i, j])
			board[i][j] = -1
			visit[i][j] = 1
		elif input[j] == '*':
			dust.append([i, j])
			board[i][j] = 1
		elif input[j] == 'o':
			cy, cx = i, j
			board[i][j] = 2

dis = [[0 for x in range(len(dust) + 1)] for y in range(len(dust) + 1)]
bfs(cy, cx)
for i in range(len(dust)):
	bfs(dust[i][0], dust[i][1])