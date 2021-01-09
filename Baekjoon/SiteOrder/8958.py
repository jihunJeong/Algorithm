t = int(input())

score = 0
total = 0

for i in range(t):
	str_input = input()

	for i in str_input:
		if i == 'O':
			score += 1
			total = total + score
		else :
			score = 0

	print(total)

	score = 0
	total = 0