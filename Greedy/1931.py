import sys
import math

"""summarize 1931
	
	- 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있다.
	- 회의실을 사용 할 수 있느 최대의 회의 수를 구하여라. 
	- 단 시작시간과 끝나는 시간이 같을 수도 있다.
	
	Input case : 
		- 첫번째 줄 : N(회의의 개수)
		- 두번째 줄 부터 N + 1 : 각 회읭 시작시간과 끝나는 시간. 0 <= T <= 2^31 - 1 (T는 자연수)

	Solution : 
		- DP 문제는 먼저 예제를 보고 Greedy Algorithm을 할지 말지 정한다.
		- Greedy가 실패했을 때 DP 정규 방법으로 넘어간다.

	Greedy에서 최적의 값을 찾기 위해서 두개의 List를 이용한다.
"""

n = int(input()) #회의의 개수

start_time = [] #Declare Dictionary type
finish_time = []

for i in range(n):
	start, finish = map(int, input().split())
	
	start_time.append(start)
	finish_time.append(finish)

"""논리 다시 짜고 접근하기
min_start = min(start_time)
min_finish = finish_time[start_time.index(min_start)]
min_index = start_time.index(min_start)
cnt = 0

while min_finish <= max(finish_time): 
	cnt += 1
	tmp_start = min_finish

	for i in range(len(start_time)):
			if min_start == start_time[i]:
				min_start = finish_time[start_time.index(min_start)] <= finish_time[i] ? min_start : finish_time[i] 
				min_index = start_time.index(min_start)
			elif tmp_start > start_time[i] and start_time > min_finish:
				tmp_start = start_time
	min_finish = finish_time[start_time.index(min_start)]	
"""

print(cnt)	
