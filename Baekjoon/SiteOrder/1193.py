N = int(input())
chk, s = 2, 0
while True:
	if s < N and N <= s + chk - 1:
		pos = N - s	
		if chk % 2 == 0:
			print("%d/%d" %(chk - pos, pos))
		else :
			print("%d/%d" %(pos, chk - pos))
		break
	s = s + chk - 1
	chk += 1