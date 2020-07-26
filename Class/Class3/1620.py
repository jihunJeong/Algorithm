import sys

n, m = map(int, sys.stdin.readline().split())
user = []
suser = [[] for _ in range(n)]
for i in range(n):
	tmp = input()
	user.append(tmp)
	suser[i] = [tmp, i+1]

suser = sorted(suser, key=lambda x: x);

for i in range(m):
	tmp = input()
	if tmp.isdigit():
		print(user[int(tmp)-1])
	else :
		left, right = 0, n-1

		while left <= right:
			mid = (left + right) // 2

			if suser[mid][0] == tmp:
				print(suser[mid][1])
				break

			elif suser[mid][0] > tmp:
				right = mid - 1
			else :
				left = mid + 1

