import sys

a = list()
n = sys.stdin.readline()

for i in range(len(n) - 1):
	a.append(n[i])

a.sort(reverse = True)

for i in range(len(a)):
	print(a[i], end = '')
