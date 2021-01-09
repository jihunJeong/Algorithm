import sys

n = int(input())
num = list(map(int, input().split()))
ans, sum = num[0], num[0]

for i in range(1, len(num)):
	if num[i] >= 0:
		if ans < 0:
			ans = num[i]
			sum = num[i]
		else :
			sum += num[i]
			ans = max(sum, ans)
	else :
		if ans >= 0 and sum + num[i] < 0:
			sum = 0
		else :
			sum += num[i]  
			ans = max(ans, num[i])
print(ans)