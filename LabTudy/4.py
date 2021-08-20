N = int(input())
arr = sorted(list(map(int,input().split())))

ans = 1
for c in arr:
    if c <= ans:
        ans += c
    else :
        break
print(ans)