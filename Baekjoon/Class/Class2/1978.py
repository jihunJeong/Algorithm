n = int(input())
num = list(map(int, input().split()))
ans = 0
for i in num:
	if i == 1:
		continue
	cnt = 0
	for j in range(2, i):
		if i % j == 0:
			cnt += 1

	if cnt == 0:
		ans += 1

print(ans)