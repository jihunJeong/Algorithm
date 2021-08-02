N = int(input())

fear = sorted(list(map(int, input().split())))

ans, count = 0, 0
for i in range(len(fear)):
    count += 1
    if fear[i] == count:
        ans += 1
        count = 0

print(ans)
