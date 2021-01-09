n = int(input())

numberInput = input()
number_list = list()

for i in numberInput:
	number_list.append(int(i))

print(sum(number_list))