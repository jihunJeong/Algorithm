import sys
import heapq

L = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))
input_list.insert(0, 0)
N = int(sys.stdin.readline())
count = []
cnt = {}
dis = dict()

for i in range(1, L + 1):
	#count[input_list[i]] = 0
	heapq.heapqpush(count, (0, input_list[i]))
	if i != L and input_list[i + 1] - input_list[i] >= 2:
		dis[i] = input_list[i + 1] - input_list[i]
dis[0] = input_list[0]

dis = sorted(dis.items(), key=lambda item: item[1])
for i in range(len(dis)):
	a = dis[i][0]
	if input_list[a + 1] - input_list[a] == 2:
		#count[input_list[a] + 1] = 0
		heapq.heappush(count, (0, input_list[a] + 1))
	for j in range(input_list[a] + 1, input_list[a + 1] - 1):
		for k in range(j + 1, input_list[a + 1]):
			for p in range(j, k + 1):
				if p not in count.keys():
					cnt[p] = 1
				else :
					cnt[p] += 1


#count = list(sorted(count.items(), key=lambda item: (item[1], item[0])))
for i in range(min(N, len(count))):
	#print(count[i][0], end=" ")
	print(heapq.heappop(count)[1], end=" ")
for i in range(N - len(count)):
	print(input_list[L] + i + 1, end=" ")
