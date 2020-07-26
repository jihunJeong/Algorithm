import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
info = [[0, 0] for _ in range(m)]
have = list(map(int, sys.stdin.readline().split()))

for i in range(m):
	info[i][0] = have[i]

info = sorted(info, key=lambda x: x[0])
for i in range(n):
	left, right = 0, m-1
	while left <= right:
		mid = (left + right) // 2
		
		if card[i] == info[mid][0]:
			info[mid][1] += 1
			break

		elif card[i] < info[mid][0]:
			right = mid -1
		else :
			left = mid + 1

for i in range(m):
	left, right = 0, m-1
	while left <= right:
		mid = (left + right) // 2
		
		if have[i] == info[mid][0]:
			print(info[mid][1], end=" ")
			break

		elif have[i] < info[mid][0]:
			right = mid -1
		else :
			left = mid + 1
print("")