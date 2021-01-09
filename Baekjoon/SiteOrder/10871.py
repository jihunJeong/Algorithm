n, x = map(int, input().split())
list_input = list(map(int, input().split()))

for i in list_input:
	if i < x:
		print(i, end=" ")
