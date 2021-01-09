import sys
from collections import deque

"""summarize 2178
	 
	- n * m 의 배열이 있다.
	- 1은 이동할 수 있는 칸, 0은 갈 수 없는 칸
	- (1, 1)에서 출발해 (n, m)으로 가는 최소의 칸 수 구해라
	
	Input :
		첫번째 줄 : N, M(2 <= N, M <= 100)
		두번째 줄 부터 N개의 줄 : 0, 1로 미로 주어짐(각각의 수는 붙어서 입력 됨)
	
	Solution :
		최솟값을 구해야 하므로 BFS가 적합하다
		visit 배열을 만들어 최소로 방문했을 때 이전 방문한 수의 1을 증가시킨다.	
"""

#Queue를 이용한 BFS 알고리즘이다.
def bfsMaze(n, m):
	bfs_dq = deque()
	bfs_dq.append([n, m])		
	
	#좌표가 이동할 수 있는 경우의 수 배열
	avl_x = [0, 1, 0, -1]
	avl_y = [-1, 0, 1, 0]

	visit[n][m] = 1
	
	while len(bfs_dq):
		arr = bfs_dq.popleft()

		for i in range(4):
			nx = arr[1] + avl_x[i]
			ny = arr[0] + avl_y[i]

			if 0 <= nx and 0 <= ny and len(maze[0]) > nx and len(maze) > ny:
				if maze[ny][nx] == 1 and visit[ny][nx] == 0:
					visit[ny][nx] = visit[arr[0]][arr[1]] + 1
					bfs_dq.append([ny, nx])
					
					if nx == len(maze[0]) - 1 and len(maze) - 1 == ny:
						return 0

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


print(visit[n - 1][m - 1])
