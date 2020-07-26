import sys

board = ["WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW"]
n, m = map(int, sys.stdin.readline().split())

inputstr = []
for i in range(n):
	temp = sys.stdin.readline()
	inputstr.append(temp)

ans = 1000
cntw, cntb = 0, 0

for i in range(n-7):
	for j in range(m-7):
		cntw, cntb = 0, 0
		for k in range(8):
			for x in range(8):
				if inputstr[i+k][j+x] != board[k][x]:
					cntw += 1
				if inputstr[i+k][j+x] != board[(k+1)%8][x]:
					cntb += 1

		ans = min(ans, cntw, cntb)

print(ans)