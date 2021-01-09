import sys
import heapq

heap = []
N = int(sys.stdin.readline())
for i in range(N):
	heapq.heappush(heap, int(sys.stdin.readline()))

for _ in range(N):
	print(heapq.heappop(heap))