import sys

N = int(sys.stdin.readline())
heap = [0] *10000
for i in range(N):
	num = int(sys.stdin.readline())
	heap[num - 1] += 1

for i in range(10000):
	for _ in range(heap[i]):
		print(i + 1)