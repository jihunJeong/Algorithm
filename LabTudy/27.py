N, X = map(int, input().split())

arr = list(map(int, input().split()))


left_index, right_index = -1, -1

start, end = 0, len(arr)-1
while start <= end:
    mid = (start + end) // 2
    if arr[mid] == X:
        left_index = mid
        end = mid - 1
    elif arr[mid] > X:
        end = mid - 1
    elif arr[mid] < X:
        start = mid + 1
        
start, end = 0, len(arr)-1
while start <= end:
    mid = (start + end) // 2
    if arr[mid] == X:
        right_index = mid
        start = mid + 1
    elif arr[mid] > X:
        end = mid - 1
    elif arr[mid] < X:
        start = mid + 1

if left_index == -1 and right_index == -1:
    print(-1)
else :
    print(right_index - left_index + 1)