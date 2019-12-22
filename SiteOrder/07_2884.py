import sys
from datetime import datetime, timedelta

h, m = map(int, sys.stdin.readline().split())

if h == 0 and m < 45:
	h = 23
	m += 15
elif m < 45:
	h -= 1
	m += 15
else :
	m -= 45

print("%d %d" %(h, m))