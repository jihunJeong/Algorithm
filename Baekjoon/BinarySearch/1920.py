import sys
import math

"""summarize 1920

	N개의 정수가 주어졌을 때 X라는 정수가 존재하는지 알아내라

	Input Case :
		첫째 줄 : N(1 <= N <= 100000)
		둘째 줄 : N개의 자연수 주어짐
		셋째 줄 : M(1 <= M <= 100000)
		넷째 줄 : M개의 자연수 주어짐

	Solution :
		주어진 배열 안에서 정해진 수를 찾는 문제이다. 
		파이썬 리스트에 있는 내장 함수를 통해 해결 하면 간편해진다.
"""

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for i in b:
	try :
		a.index(i)
		print("1")
	except ValueError:
		print("0")
