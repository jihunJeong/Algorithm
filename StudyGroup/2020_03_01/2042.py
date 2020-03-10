import math

def init(node, start, end):
	if start == end:
		tree[node] = num[start]
		return tree[node]
	else :
		tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
		return tree[node]

def sum(node, start, end, left, right):
	if left > end or right < end:
		return 0
	if left <= start and end <= right:
		return tree[node]
	ret = sum(node*2, start, (start+end)//2, left, right) + sum(node*2+1, (start+end)//2+1, end, left, right)
	return ret

def update(node, start, end, index, diff):
	if index < start or end < index:
		return 
	tree[node] = tree[node] + diff
	if start != end:
		update(node*2, start, (start+end)//2, index, diff)
		update(node*2+1, (start+end)//2+1, end, index, diff)
		
N, M, K = map(int, input().split())
num = list()
tree = [0] * (N * 4)
for _ in range(N):
	num.append(int(input()))



init(1, 0, N-1)
for i in range(M + K):
	a, b, c = map(int, input().split())
	if a == 1:
		diff = c - num[b - 1]
		num[b-1] = c
		update(1, 0, N-1, b-1, diff)
		print(tree)
	else :
		print(sum(1, 0, N-1, b-1, c-1))