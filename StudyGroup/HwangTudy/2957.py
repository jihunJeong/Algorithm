import heapq

def trfind():
	
def insert(node, num, cnt):
	cnt += 1
	if num < heapfind(node)[1]:
		if heapfind(2*node)[1] == -1:
			print(cnt)
			tree[2*node] = num
		else :
			insert(2*node, num, cnt)
	else :
		if tree[2*node+1] == -1:
			print(cnt)
			tree[2*node+1] = num
		else :
			insert(2*node+1, num, cnt)

N = int(input())
for i in range
cnt = 0
heap = []

for i in range(N):
	insert(1, int(input()), cnt)