import sys

UP = 1
DWON = 2
RIGHT = 3
LEFT = 4

def fishing(fishking):
	tmp = 0
	for y in range(len(sea)):
		if sea[y][fishking] != 0: 
			tmp = sea[y][fishking]
			sea[y][fishking] = 0
			shark[tmp][2] = 0
			return tmp
	return 0

def eatShark():

def moveShark():
	for i in range(1, len(shark) + 1):
		if shark[i][2] != 0:
			if shark[i][3] == UP:
				new_y = shark[i][0] - shark[i][2]
				new_x = shark[i][1]
			if shark[i][3] == DWON:
				new_y = shark[i][0] + shark[i][2]
				new_x = shark[i][1]
			if shark[i][3] == RIGHT:
				new_y = shark[i][0]
				new_x = shark[i][1] + shark[i][2]
			if shark[i][3] == LEFT:
				new_y = shark[i][0]
				new_x = shark[i][1] - shark[i][2]
			
r, c, m = map(int, sys.stdin.readline().split())
sea = [[0 for x in range(c)] for y in range(r)]
shark = [[0,0,0,0,0]]
total_size = 0

for i in readline(m):
	y, x, s, d, z = map(int, sys.stdin.readline().split())
	total_size = total_size + z
	sea[y][x] = i + 1
	shark.append([y, x, s, d, z])

fishking = -1
while fishKing < c:
	fishking = fishking + 1

	num_shark = fishing(fishKing)
	total_size = total_size - shark[num_shark][3] 

	moveShark()