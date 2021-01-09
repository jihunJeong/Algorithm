host, pre, dis = input().split()
dis = int(dis)
pre = list(pre)
N = int(input())
ans = list()
for i in range(N):
	cus, sub, r = input().split()
	sub = list(sub)
	r = int(r)
	for j in range(len(sub)):
		if sub[j] in pre and r <= dis:
			ans.append(cus)
			break
if len(ans) == 0:
	print("No one yet")
else :
	ans.sort()
	for i in range(len(ans)):
		print(ans[i])