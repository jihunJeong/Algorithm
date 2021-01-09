import math
import sys

c = int(sys.stdin.readline())

for i in range(c):
	input_list = list(map(int, sys.stdin.readline().split()))

	sum_input = sum(input_list) - input_list[0]
	avg = sum_input / input_list[0]

	cnt_over = 0

	for i in range(1, len(input_list)):
		if avg < input_list[i]:
			cnt_over += 1

	percent = (cnt_over / input_list[0]) * 100

	print("%.3f%%" %percent)	#FORMAT 함수에 대해 배움
