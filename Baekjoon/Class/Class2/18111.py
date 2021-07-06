n, m, b = map(int, input().split())

minimum, maximum, total = 257, -1, 0
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    arr_min, arr_max = min(arr[i]), max(arr[i])
    if arr_min < minimum:
        minimum = arr_min
    if arr_max > maximum:
        maximum = arr_max
    total += sum(arr[i])

pos_h = min((total+b) // (n*m),256)
ans_t, ans_h = 1000000000, 0
for i in range(minimum, min(maximum, pos_h)+1):
    t = 0 
    for j in range(n):
        for k in range(m):
            if arr[j][k] > i:
                t += (arr[j][k]-i) * 2
            elif arr[j][k] < i:
                t += (i-arr[j][k])
    
    if ans_t > t:
        ans_t = t
        ans_h = i
    elif ans_t == t and ans_h < i:
        ans_h = i

print(f"{ans_t} {ans_h}")
