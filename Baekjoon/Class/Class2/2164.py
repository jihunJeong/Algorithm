n = int(input())
num = []
for i in range(1,n+1):
	num.append(i)

s, e = 0, n-1
chk = False
while s != e:
	for i in range(s, e+1):
		if chk:
			num.append(num[s])
			s = s+1
			e = e+1
			chk = False
		else :
			s = s+1
			chk = True

print(num[s])