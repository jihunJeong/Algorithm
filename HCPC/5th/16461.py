def under(num):
	if num < 144:
		num = 146
	return num
def upper(num):
	if num > 146:
		num = 144
	return num

T = int(input())
for i in range(T):
	a, b, now, tar = input().split()
	a, b, tar = float(a), float(b), float(tar)
	ans = [[a, b, 0]]
	ret = 6
	for i in range(5):
		ans.append([round(upper(ans[i][0]+0.02),3),round(upper(ans[i][1]+0.02),3),i+1])
	ans.append([round(under(ans[0][0]-0.02),3),round(under(ans[0][1]-0.02),3),1])
	for i in range(6, 10):
		ans.append([round(under(ans[i][0]-0.02),3),round(under(ans[i][1]-0.02),3),i - 4])
	
	for i in range(len(ans)):
		if tar == ans[i][0]:
			if now == "B":
				ret = min(ret, ans[i][2]+1)
			else :
				ret = min(ret, ans[i][2])
		if tar == ans[i][1]:
			if now == "A":
				ret = min(ret, ans[i][2]+1)
			else :
				ret = min(ret, ans[i][2])

	print(ret)