arr = list(input().split('-'))

ans = 0
for i in range(len(arr)):
    inner_arr = list(map(int, arr[i].split('+')))
    if i == 0:
        ans += sum(inner_arr)
    else :
        ans -= sum(inner_arr)

print(ans)