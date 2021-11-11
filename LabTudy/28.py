N = int(input())

arr = list(map(int, input().split()))
start, end = 0, len(arr) - 1
flag = False
while start <= end:
    mid = (start + end) // 2

    if arr[mid] == mid:
        print(mid)
        flag = True
        break
    elif arr[mid] > mid:
        end = mid - 1
    elif arr[mid] < mid:
        start = mid + 1

if not flag:
    print(-1)
