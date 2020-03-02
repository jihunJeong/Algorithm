import sys

N, E = map(int, sys.stdin.readline().split())
edge = list()

for i in range(E):
	a, b, c = map(int, sys.stdin.readline().split())
	edge.append([[a, b], c])
s, e = map(int, sys.stdin.readline().split())