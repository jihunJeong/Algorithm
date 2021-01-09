import math
import sys

m, n = map(int, sys.stdin.readline().split())

def is_prime(i):
	if i == 1:
		return False
	
	
	for j in range(2, round(i ** 0.5) + 1):
		if i % j == 0:
			return False
	return True

for i in range(m, n + 1):
	if is_prime(i):
		print(i)
