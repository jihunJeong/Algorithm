import sys

L = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
count = {}
dis = dict()

for i in range(L):
	count[input_list[i]] = 0
	if i != L - 1 and input_list[i + 1] - input_list[i] >= 2:
		dis[i] = input_list[i + 1] - input_list[i]

print(type(dis))
dis = sorted(dis.items(), key=lambda item: item[1])
for i in range(len(dis)):
	a = dis[0][i]
	if input_list[a + 1] - input_list[a] == 2:
		count[input_list[a] + 1] = 0

	for j in range(input_list[a], input_list[a + 1]):
		for k in range(j + 1, input_list[a + 1] + 1):
			for p in range(j, k + 1):
				if p not in count.keys():
					count[p] = 1
				else :
					count[p] += 1

for j in range(1, input_list[0] - 1):
	print(j)
	for k in range(j + 1, input_list[0]):
		print(k)
		for p in range(j, k + 1):
			if p not in count.keys():
				count[p] = 1
			else :
				count[p] += 1

count = list(sorted(count.items(), key=lambda item: (item[1], item[0])))
print(count)
for i in range(len(count)):
	print(count[i][0], end=" ")

for i in range(N - len(count)):
	print(input_list[L - 1] + i + 1, end=" ")
