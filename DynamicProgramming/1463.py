"""
	Solution : 
		1. 가장 큰 수로 먼저 나누는 것이 빠르게 1에 도달한다 -> 실패
			Greedy Algorithm을 하면 10에서 반례가 생긴다.

		2. n의 값이 주어질 때 n - 1 까지의 값을 계산해 list에 저장해 max값 비교하면서 
		   n의 값을 구한다.
"""

import sys
import math

def countNum(n, count_list):
	if n == 1 or n == 2 or n == 3:
		return 0
	elif n % 2 == 0 and n % 3 == 0:
		return min(count_list[n // 2] + 1, count_list[n // 3] + 1, count_list[n - 1] + 1)
	elif n % 2 == 0:
		return min(count_list[n // 2] + 1, count_list[n - 1] + 1)
	elif n % 3 == 0:
		return min(count_list[n // 3] + 1, count_list[n - 1] + 1)
	else :
		return count_list[n  - 1] + 1

n = int(input()) #Number

count_list = [0, 0, 1, 1]
k = 4

while k <= n:
	count_list.append(countNum(k, count_list))
	k += 1

print(count_list[n])	
