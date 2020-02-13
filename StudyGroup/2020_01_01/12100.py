import sys
import copy

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

def checkSameBlock(y, x, action):
	if board[y][x] == 0:
		return False
	if action == UP and board[y][x] == board[y + 1][x]:
		return True
	if action == DOWN and board[y][x] == board[y - 1][x]:
		return True
	if action == LEFT and board[y][x] == board[y][x + 1]:
		return True
	if action == RIGHT and board[y][x] == board[y][x - 1]:
		return True
	3
	return False

def compactBoard(action):
 	if action == UP:
 		for y in range(size - 1):
 			for x in range(size):
 				if board[y][x] == 0:
 					board[y][x] = board[y + 1][x]
 					board[y + 1][x] = 0
 	if action == DOWN:
 		for y in range(size - 1, 0, -1):
 			for x in range(size):
 				if board[y][x] == 0:
 					board[y][x] = board[y - 1][x]
 					board[y - 1][x] = 0
 	if action == LEFT:
 		for x in range(size - 1):
 			for y in range(size):
 				if board[y][x] == 0:
 					board[y][x] = board[y][x + 1]
 					board[y][x + 1] = 0
 	if action == RIGHT:
 		for x in range(size - 1, 0, -1):
 			for y in range(size):
 				if board[y][x] == 0:
 					board[y][x] = board[y][x - 1]
 					board[y][x - 1] = 0

def joinNumber(y, x, action):
	board[y][x] = board[y][x] * 2

	if action == UP:
		board[y + 1][x] = 0
	if action == DOWN:
		board[y - 1][x] = 0
	if action == LEFT:
 		board[y][x + 1] = 0
	if action == RIGHT:
		board[y][x - 1] = 0

def goUp(size):
	for y in range(size - 1):
		for x in range(size):
			if checkSameBlock(y, x, UP) == True:
				joinNumber(y, x, UP)
	compactBoard(UP)

def goDown(size):
	for y in range(size - 1, 0, -1):
		for x in range(size):
			if checkSameBlock(y, x, DOWN) == True:
				joinNumber(y, x, DOWN)
	compactBoard(DOWN)

def goLeft(size):
	for x in range(size - 1):
		for y in range(size):
			if checkSameBlock(y, x, LEFT) == True:
				joinNumber(y, x, LEFT)
	compactBoard(LEFT)

def goRight(size):
	for x in range(size - 1, 0, -1):
		for y in range(size):
			if checkSameBlock(y, x, RIGHT) == True:
				joinNumber(y, x, RIGHT)
	compactBoard(RIGHT)

def checkMax(size):
	maxNumber = 0
	for y in range(size):
		for x in range(size):
			maxNumber = max(maxNumber, board[y][x])
	return maxNumber

def goFunction(size, action):
	if action == UP:
		goUp(size)
	if action == DOWN:
		goDown(size)
	if action == LEFT:
		goLeft(size)
	if action == RIGHT:
		goRight(size)

size = int(sys.stdin.readline())
original_board = list()
board = list()
maxNumber = 0

for i in range(size):
	temp = list(map(int, sys.stdin.readline().split()))
	original_board.append(temp)

for i in range(1, 5):
	for j in range(1, 5):
		for k in range(1, 5):
			for n in range(1, 5):
				for m in range(1, 5):
					board = copy.deepcopy(original_board)
					goFunction(size, i)
					goFunction(size, j)
					goFunction(size, k)
					goFunction(size, n)
					goFunction(size, m)
					maxNumber = max(maxNumber, checkMax(size))
print(maxNumber)
