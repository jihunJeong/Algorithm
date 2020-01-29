import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
matrix = list()

for i in range(1, n + 1):
	for j in range(1, n + 1):
		matrix.append(i * j)

matrix.sort()
print(matrix[6])