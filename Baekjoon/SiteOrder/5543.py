a, b = 2001, 2001
for i in range(3):
	a = min(a, int(input()))
for i in range(2):
	b = min(b, int(input()))
print(a + b - 50)