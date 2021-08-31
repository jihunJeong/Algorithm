from collections import defaultdict

N, M = map(int, input().split())
li = list(map(int, input().split()))

info = defaultdict(int)
total = len(li)
for n in li:
    info[n] += 1

ans = 0
for key in info.keys():
    cnt = info[key]
    total -= cnt
    ans += cnt * total

print(ans)