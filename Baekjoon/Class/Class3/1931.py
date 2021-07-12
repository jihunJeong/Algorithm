N =  int(input())

meet = []
for _ in range(N):
    meet.append(list(map(int, input().split())))

meet = sorted(meet, key=lambda x : (x[1], x[0]))
ans, last = 0, 0

for s, e in meet:
    if last <= s:
        ans += 1
        last = e
print(ans)