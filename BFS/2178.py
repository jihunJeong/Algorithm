import sys
from collections import deque


def bfsMaze(n, m):
	global glength
	bfs_dq = deque([])
	bfs_dq.append([n, m])		
	avl_x = [0, 1, 0, -1]
	avl_y = [-1, 0, 1, 0]

	visit[n][m] = 1
	glength = 1
	#glenth의 가감에 대해 좀 더 생각을 하자
	#특정 점을 갔을 때 발생하는 visit 배열을 이용하면 된다. 같은 항렬을 이용
	while len(bfs_dq):
		arr = bfs_dq.popleft()
		cnt = -1

		for i in range(4):
			nx = arr[1] + avl_x[i]
			ny = arr[0] + avl_y[i]

			if 0 <= nx and 0 <= ny and len(maze[0]) > nx and len(maze) > ny:
				if maze[ny][nx] == 1 and visit[ny][nx] == 0:
					visit[ny][nx] = 1
					glength += 1
					bfs_dq.append([ny, nx])
					cnt += 1

					if nx == len(maze[0]) - 1 and len(maze) - 1 == ny:
						return 0

		if cnt > 0:
			glength = glength - cnt

n, m = map(int, sys.stdin.readline().split())
maze = [[0 for x in range(m)] for y in range(n)]
visit = [[0 for x in range(m)] for y in range(n)]

for i in range(n):
	strinput = sys.stdin.readline()
	for j in range(m):
		maze[i][j] = int(strinput[j])

#Start Bfs Algorithm
for i in range(n):
	for j in range(m):
		if visit[i][j] == 0 and maze[i][j] == 1:
			bfsMaze(i, j)


print(glength)
