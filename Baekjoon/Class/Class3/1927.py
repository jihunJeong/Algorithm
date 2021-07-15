import heapq
import sys

N = int(sys.stdin.readline())
hp = []
for _ in range(N):
    n = int(sys.stdin.readline())

    if n == 0:
        if len(hp) == 0:
            print(0)
        else :
            print(heapq.heappop(hp))
    else :
        heapq.heappush(hp, n)