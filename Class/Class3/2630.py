import sys

sys.setrecursionlimit(10**6)

wcnt = 0
bcnt = 0

def recursive(y, x, n):
	global wcnt, bcnt
	if n == 1:
		if board[y][x] == 1:
			bcnt += 1
			return 0
		else :
			wcnt += 1
			return 0

	cnt = 0		
	for i in range(y, y+n):
		for j in range(x, x+n):
			if board[i][j] == 1:
				cnt += 1
	
	if cnt == 0:
		wcnt += 1
	elif cnt == n*n:
		bcnt +=1
	else :
		half = n //2
		recursive(y, x, half)
		recursive(y+half, x, half)
		recursive(y, x+half, half)
		recursive(y+half, x+half, half)


if __name__ == "__main__":
	n = int(sys.stdin.readline())
	board = [[] for _ in range(n)]
	for i in range(n):
		tmp = list(map(int, sys.stdin.readline().split()))
		board[i] = tmp

	recursive(0, 0, n)
	print(wcnt)
	print(bcnt)
