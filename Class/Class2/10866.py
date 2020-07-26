from collections import deque

num = deque()
n = int(sys.stdin.readline())
while n:
	n -= 1
	arr = list(sys.stdin.readline().split())
	if arr[0] == "push_front":
		num.appendleft(int(arr[1]))
	elif arr[0] == "push_back":
		num.append(int(arr[1]))
	elif arr[0] == "pop_front":
		if not num:
			print(-1)
		else :
			print(num.popleft())
	elif arr[0] == "pop_back":
		if not num:
			print(-1)
		else :
			print(num.pop())
	elif arr[0] == "size":
		print(len(num))
	elif arr[0] == "empty":
		if not num:
			print(1)
		else :
			print(0)
	elif arr[0] == "front":
		if not num:
			print(-1)
		else :
			print(num[0])
	elif arr[0] == "back":
		if not num:
			print(-1)
		else :
			print(num[-1])