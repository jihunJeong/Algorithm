N = int(input())
people = list(map(int, input().split()))

tree = [[] for y in range(N+1)]
for i in range(N-1):
	s, e = map(int, input().split())
	tree[s].append(e)
	tree[e].append(s)

dp = [[0 for x in range(2)] for y in range(N+1)]
