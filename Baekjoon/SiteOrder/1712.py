import sys

"""
	매년 A의 고정 금액
	노트북 한 대 당 B의 금액
"""

a, b, c = map(int, sys.stdin.readline().split())

if c - b <= 0:
	print(-1)
else :
	cnt = a // (c - b)
	print(cnt + 1)