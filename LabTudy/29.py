N, C = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr = sorted(arr)
start = 1
end = arr[-1] - arr[0]
answer = 0
while start <= end:
    mid = (start + end) // 2

    s = arr[0]
    count = 1
    for i in range(len(arr)):
        if i == 0:
            continue
        
        if arr[i] - s >= mid:
            count += 1
            s = arr[i]
    
    if count >= C:
        answer = mid
        start = mid + 1
    elif count < C:
        end = mid - 1

print(answer)