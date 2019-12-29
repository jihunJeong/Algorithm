import sys

n = int(sys.stdin.readline())

new_number = -1
cnt = 0
n1 = n // 10
n2 = n % 10

while True:
	add =  n1 + n2
	new_number = n2 * 10 + add % 10
	cnt += 1

	if n == new_number:
		print(cnt)
		break

	n1 = new_number // 10
	n2 = new_number % 10
