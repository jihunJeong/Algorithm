import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num = sorted(num, key=lambda x: x)
ans, time = 0, 0
for i in range(n):
	ans = ans + num[i] + time
	time = time + num[i]

print(ans)