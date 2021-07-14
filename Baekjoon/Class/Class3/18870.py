N = int(input())
li = list(map(int, input().split()))
set_li = sorted(list(set(li)))

info = dict()
for i, n in enumerate(set_li):
    info[n] = i

for n in li:
    print(info[n], end=" ")