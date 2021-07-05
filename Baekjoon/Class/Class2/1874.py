cnt = int(input())

arr = []
for i in range(cnt):
    n = int(input())
    arr.append(n)

number, idx = 1, 0
s, ans = [], []
flag = True
for i in range(2*cnt):
    if len(s) == 0 or arr[idx] != s[-1]:
        if number > cnt:
            flag = False
            break
        s.append(number)
        number+=1
        ans.append("+")
    elif arr[idx] == s[-1]:
        s.pop()
        idx += 1
        ans.append("-")

if flag:
    for i in ans:
        print(i)
else :
    print("NO")
