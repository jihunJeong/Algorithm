while True:
	string = input()
	if string == "0":
		break
	left, right = 0, len(string)-1
	
	chk = True
	while left <= right:
		if string[left] != string[right]:
			chk = False
			break
		left += 1
		right -= 1

	if chk:
		print("yes")
	else :
		print("no")