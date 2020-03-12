while True:
	a, b, c = map(int, input().split())
	if a == 0 and b == 0 and c == 0:
		break

	ans = a**2 + b**2 + c**2

	if ans == max(a, b, c)**2 * 2 and max(a,b,c)*2 < a+b+c:
		print("right")
	else :
		print("wrong")