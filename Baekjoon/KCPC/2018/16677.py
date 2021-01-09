def lcs(str1, str2):
	dp = [[0 for x in range(len(str1)+1)] for y in range(len(str2)+1)]
	for i in range(1, len(str2)+1):
		for j in range(1, len(str1)+1):
			if str2[i-1] == str1[j-1]:
				dp[i][j] = dp[i - 1][j - 1] + 1
			else :
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	if dp[len(str2)][len(str1)] != len(str1):
		return 0
	else :
		return 1

m = input()
N = int(input())
ans = 0
ret = ""
for i in range(N):
	w, g = input().split()
	g = int(g)
	if lcs(m, w):
		if ans < g/abs(len(m)-len(w)):
			ret = w
			ans = g/abs(len(m)-len(w))
if ans == 0:
	print("No Jam")
else :
	print(ret)