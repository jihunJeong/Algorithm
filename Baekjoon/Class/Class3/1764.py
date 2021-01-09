import sys

n, m = map(int, sys.stdin.readline().split())

dset = set()
for i in range(n):
	tmp = input()
	dset.add(tmp)

bset = set()
for i in range(m):
	tmp = input()
	bset.add(tmp)

ans = list(dset.intersection(bset))
ans = sorted(ans, key=lambda x: x)
print(len(ans))
for i in ans:
	print(i)