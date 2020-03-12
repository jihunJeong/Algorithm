N = int(input())
ans = 0
for i in range(1, N):
	sp = list(str(i))
	sum = 0
	for j in range(len(sp)):
		sum += int(sp[j])
	if i + sum == N:
		ans = i
		break
print(ans)