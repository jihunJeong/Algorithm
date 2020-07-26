n, k = map(int, input().split())
num = [[] for _ in range(n)]
index = -1

for i in range(n):
	num[i] = [i+1, 0]

cnt = 0
print("<", end="")
while cnt < n:
	i = 0
	while i < k:
		index += 1
		if num[index % n][1] == 0:
			i += 1
	print(str(num[index%n][0]), end="")
	num[index%n][1] = 1
	cnt += 1
	if cnt != n:
		print(", ", end="")
	else :
		print(">")
