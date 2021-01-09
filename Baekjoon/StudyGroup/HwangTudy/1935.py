N = int(input())
st = input()
num = list()
for i in range(N):
	num.append(int(input()))

stack = []
for i in range(len(st)):
	if st[i] == "*":
		a = stack.pop()
		b = stack.pop()
		stack.append(b*a)
	elif st[i] == "/":
		a = stack.pop()
		b = stack.pop()
		stack.append(b/a)
	elif st[i] == "+":
		a = stack.pop()
		b = stack.pop()
		stack.append(b+a)
	elif st[i] == "-":
		a = stack.pop()
		b = stack.pop()
		stack.append(b-a)
	else :
		stack.append(num[ord(st[i])-65])
		
print(format(stack[0], '.2f'))