def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a%b)

a, b = map(int, input().split())
gcdn = gcd(max(a, b),min(a, b))
lcm = gcdn * (a // gcdn) * (b // gcdn)

print(gcdn)
print(lcm)