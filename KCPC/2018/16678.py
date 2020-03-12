N = int(input())
score = list()
for i in range(N):
	score.append(int(input()))
score.sort()
ans = 0
tar = 1
for i in range(N):
	if score[i] >= tar:
		ans += score[i] - tar
		tar +=1

print(ans)