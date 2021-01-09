import sys
import math

"""summarize 2798

	2798 : 블랙잭
		- 주어진 n개의 정수 들 중 3개를 골라 M을 넘지 않으면서
		- M과 가장 가까운 값을 구해라
	
	Input case :
		첫 번째 줄 : N, M
		두 번쨰 줄 : N개의 정수
	
	Solve :
		Brute Force로 해결
	
"""

def BlackJack():
	n, m = map(int, sys.stdin.readline().split())

	number_list = list(map(int, sys.stdin.readline().split()))
	number_list.sort()
	
	sum = 0
	max_number = 0

	for  i in range(n - 2):
		for j in range(i + 1, n - 1):
			for k in range(j + 1, n):
				sum = number_list[i] + number_list[j] + number_list[k]
				
				if sum <= m and sum > max_number:
					max_number = sum

	print(max_number)
	return 0			

BlackJack()	