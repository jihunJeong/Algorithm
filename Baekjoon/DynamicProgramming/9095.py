T = int(input())
ans = [0] * 11
ans[0] = 1
ans[1] = 2
ans[2] = 4

for i in range(3, 11):
	ans[i] = ans[i-3] + ans[i-2] + ans[i-1]

for i in range(T):
	inp = int(input())
	print(ans[inp-1])