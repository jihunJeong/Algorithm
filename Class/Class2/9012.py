t = int(input())

while t:
	stack = []
	string = input()
	chk = True
	for i in string:
		if i == "(":
			stack.append(i)

		else :
			if not stack:
				chk = False
				break
			pstr = stack.pop()
			if pstr != "(":
				chk = False
				break
	t -= 1

	if chk and not stack:
		print("YES")
	else :
		print("NO")