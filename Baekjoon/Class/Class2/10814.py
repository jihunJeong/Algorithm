n = int(input())
info = [[] for y in range(n)]

for i in range(n):
	age, name = input().split()
	info[i] = [age, name]

info = sorted(info, key=lambda x: int(x[0]))
for i in range(n):
	print(info[i][0] + " " + info[i][1])