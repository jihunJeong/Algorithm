"""
	Solution :

	문제를 보면 0의 타일 갯수는 이제 무조건 짝수 개이다. 여기에 1의 타일 갯수를 더한 것이 총 N개
	N일 때 타일의 갯수는 N - 1에서 1의 타일을 붙이는 경우와  N - 2에서 00의 타일을 붙이는 경우의 합이다.
	따라서 D(N) = D(N - 1) + D(N - 2)가 성립한다.

	

	Dynamic Programming
	
	Factorial 계산을 할 때 Factorial(n) = n * Factorial(n - 1) 이므로 factorial 값을 계산해서
	저장해 놓으면 빠른 처리 시간을 보여준다
"""

import sys

sys.setrecursionlimit(100000000)

def CountTile(dic, n) :
	"""
	if n not in dic :
		result = (CountTile(dic, n - 1) % 15746) + (CountTile(dic, n - 2) % 15746)
		dic[n] = result % 15746

	return dic[n]
	"""

	for i in range(3 , n + 1) :
		dic[i] = (dic[i - 2] + dic[i - 1]) % 15746


n = int(input()) #Count of tile

dic = [0] * 1000001
dic[1] = 1
dic[2] = 2
 
CountTile(dic, n)

print(dic[n])
