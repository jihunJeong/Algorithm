import sys
import math

"""summarize 2455
	
	- 4개의 기차역이 있다.
	- 출발부터 종착까지 사람이 가장 많을 떄를 구하라

	Input case :
		내린 사람 수와 탄 사람 수가 4개의 줄에 걸쳐 입력 됨
	
	Solution : 
		최대값 M을 저장하면서 for 문을 돌린다.
"""

max_people = 0		#최대값 
current_people = 0

for i in range(4):
	out, get = map(int, sys.stdin.readline().split())
	
	current_people -= out
	current_people += get

	if max_people < current_people:
		max_people = current_people


print(max_people)
