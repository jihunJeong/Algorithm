string = list(input().rstrip())
ans = [-1] * 26

for i in range(len(string)):
	if ans[ord(string[i]) - 97] == -1:
		ans[ord(string[i]) - 97] = i

for i in range(26):
	print(ans[i], end=" ")
print("")