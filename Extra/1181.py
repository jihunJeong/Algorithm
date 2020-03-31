N = int(input())
dic = []
chk = []
for i in range(N):
	inp = input()
	if inp not in chk:
		chk.append(inp)

for i in range(len(chk)):
	dic.append([len(chk[i]), chk[i]])
dic = sorted(dic, key=lambda x: (x[0], x[1]))

for i in range(len(dic)):
	print(dic[i][1])