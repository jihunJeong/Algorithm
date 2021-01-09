t = int(input())

for i in range(t):
	num, input_str = input().split()

	for j in input_str:
		print(j * int(num), end="")

	print(" ")