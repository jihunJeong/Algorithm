import sys

"""summarize 1065
	
	- 정수 X의 자리수가 등차수열이면 그 수를 한수라고 한다.
	- N이 주어졌을 때 N보다 작거나 같은 한수의 개수 출력

	Input : 
		첫번째 줄 : N(1 <= N <= 1000)

	Solution :
		우선 1부터 N까지 다 조사하는 방법을 해본다.
"""

n = int(sys.stdin.readline())
cnt = 0			# 한수의 개수

if n == 1000:	# 1000은 한수가 아니기 때문에 후에 나오는 알고리즘의 간편성을 위해 999로 바꿔준다.
	n = 999

if n <= 99:		# 100보다 작은 모든 수는 한수이다.
	cnt = n
else :
	cnt = 99

	for i in range(100, n + 1):
		number_100 = i // 100
		number_10 = (i - number_100 * 100) // 10
		number_1 = i - number_100 * 100 - number_10 * 10

		if 2 * number_10 == number_100 + number_1:
			cnt += 1

print(cnt)
