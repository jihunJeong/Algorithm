number = list(map(int, list(input())))

ans = number[0]
for n in number[1:]:
    if ans == 0:
        ans += n
    elif n == 0:
        ans += n
    else :
        ans *= n

print(ans)