N = int(input())
chk = 1
count = 1

while True:
	chk = chk * 10 + 1
	if chk > N:
		break
	count += 1
print(count)