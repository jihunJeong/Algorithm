n = int(input())
cord = [[] for y in range(n)]

for i in range(n):
	x, y = map(int, input().split())
	cord[i] = [x, y]

cord = sorted(cord, key=lambda x: (x[0], x[1]))
for i in range(n):
	print("{} {}".format(cord[i][0], cord[i][1]))