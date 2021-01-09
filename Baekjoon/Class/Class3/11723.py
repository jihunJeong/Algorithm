import sys

m = int(sys.stdin.readline())

num = set()
while m:
	m -= 1
	inputstr = list(sys.stdin.readline().split())

	if inputstr[0] == "add":
		num.add(int(inputstr[1]))
	elif inputstr[0] == "remove":
		num.discard(int(inputstr[1]))
	elif inputstr[0] == "check":
		if int(inputstr[1]) in num:
			print(1)
		else :
			print(0)
	elif inputstr[0] == "toggle":
		if int(inputstr[1]) in num:
			num.discard(int(inputstr[1]))
		else :
			num.add(int(inputstr[1]))
	elif inputstr[0] == "all":
		num = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13, 14, 15, 16, 17, 18, 19, 20}
	elif inputstr[0] == "empty":
		num = set()