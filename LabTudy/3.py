num = list(map(int, list(input())))

start = num[0]
info = {0:0, 1:0}
info[start] = 1
for n in num:
    if n != start:
        start = n
        info[n] += 1

print(min(info[0], info[1]))