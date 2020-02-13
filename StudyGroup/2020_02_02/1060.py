import sys

L = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
count = {}

for i in range(L):
	count[input_list[i]] = 0
	