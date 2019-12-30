import sys

t = int(sys.stdin.readline())

for i in range(t):
	n, m = map(int, sys.stdin.readline().split())

	if n >= 12 and m >= 4:
		print(m * 11 + 4)
	else :
		print(-1)