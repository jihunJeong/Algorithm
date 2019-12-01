"""
	Solution :
		마지막 n번째 선택을 할 때 d(n - 1)까지의 최솟값에서 
		n번째의 합을 구해 그 중 최솟값을 d(n)에 저장한다.

		Dynamic Programming을 이용해 값을 저장해 나간다.
"""
import copy
import math

def Rgb(home_list , n , min_cost) :
	if n == 1 :
		min_cost = copy.deepcopy(home_list[0])
		return min_cost

	else :
		n -= 1
		min_cost = Rgb(home_list , n , min_cost)
		tmp_cost = [0] * 3
		tmp_cost = copy.deepcopy(min_cost)
		min_cost[0] = min(tmp_cost[1] + home_list[n][0] , tmp_cost[2] + home_list[n][0])	
		min_cost[1] = min(tmp_cost[0] + home_list[n][1] , tmp_cost[2] + home_list[n][1])
		min_cost[2] = min(tmp_cost[0] + home_list[n][2] , tmp_cost[1] + home_list[n][2])
		return min_cost

n = int(input()) #N개의 집

home_list = [[0 for j in range(3)] for i in range(n)]
min_cost = [0] * 3

for i in range(n) :
	home_list[i][0] , home_list[i][1] , home_list[i][2] = map(int, input().split())

min_cost = Rgb(home_list , n , min_cost)

print(min(min_cost[0] , min_cost[1] , min_cost[2]))
