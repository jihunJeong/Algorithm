"""
	Solution ::
		Use Greedy Algorithm

	Greedy Algorithm : 
		- Select best option in present situation
		- This can be applied specific case such as unlimit selecttion
"""

import sys
import math

n, k = map(int, input().split())
list_value_coin = []

find_key = -1
num_coin = 0

for i in range(n):
	value = int(input())
	list_value_coin.append(value)

	if value < k:
		find_key += 1

while k > 0:
	num_coin += k // list_value_coin[find_key]
	k = k % list_value_coin[find_key]
	find_key -= 1

print (num_coin)
