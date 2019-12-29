import math

a = int(input())
b = int(input())
c = int(input())

total = str(a * b * c)
count_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for i in range(len(total)):
	cnt = count_dict[int(total[i])]
	cnt += 1
	count_dict[int(total[i])] = cnt

for i in count_dict.values():
	print(i)
