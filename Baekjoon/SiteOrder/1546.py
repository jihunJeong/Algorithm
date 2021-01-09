N = int(input())
score = list(map(int, input().split()))
top = max(score)
for i in range(len(score)):
	score[i] = score[i] / top * 100
all = sum(score)
print(all / N)