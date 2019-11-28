import sys

for i in range(int(input())) :
	h, w, n = map(int, input().split()) #height, weidth, number of people

	if n % h == 0:
	 	print (int(n // h + h * 100))

	else :
		print (int(n % h * 100) + int(n // h + 1))