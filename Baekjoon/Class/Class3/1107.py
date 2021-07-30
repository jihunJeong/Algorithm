import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().split()))

info = {key:1 for key in range(10)}
for b in broken:
    info[b] = 0


ans = 100000000
ans = min(ans, abs(100-N))

for i in range(1000000):
    flag = True
    for j in str(i):
        if info[int(j)] == 0:
            flag = False
            break
    if flag:
        ans = min(ans, len(str(i))+abs(i-N))

print(ans)