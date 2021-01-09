N = int(input())

cnt, s = 1, 1
while True:
	if N <= s:
		break
	s = s + 6 * cnt
	cnt += 1

print(cnt)