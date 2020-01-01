n = int(input())
input_list = list()

for i in range(n):
	input_list.append(int(input()))

input_list.sort()

for i in input_list:
	print(i)