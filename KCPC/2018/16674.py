st = list(input())
N = list()
for i in range(len(st)):
	N.append(int(st[i]))
cnt2 = N.count(2)
cnt0 = N.count(0)
cnt1 = N.count(1)
cnt8 = N.count(8)

if cnt2 + cnt0 + cnt1 + cnt8 == len(N):
	if cnt2 > 0 and cnt0 > 0 and cnt1 > 0 and cnt8 > 0:
		if cnt2 == cnt0 and cnt0 == cnt1 and cnt1 == cnt8:
			print(8)
		else :
			print(2)
	else :
		print(1)
else :
	print(0)