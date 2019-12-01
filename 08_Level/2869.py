import sys

"""
	단순한 Math를 이용한 문제이다
"""

"""
cnt, sum = 0, 0

climb, slip, height = map(int,sys.stdin.readline().split())

while True :
	cnt += 1
	sum += climb

	if sum >= height :
		break

	sum -= slip

print (cnt)
"""

climb, slip, height = map(int, input().split())

min_days = (height - climb) / (climb - slip)

if min_days == round(min_days):
        print (int(min_days + 1))
else :
        print (round(min_days + 1.5))

