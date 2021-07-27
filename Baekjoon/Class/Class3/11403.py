import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    inp = list(map(int, sys.stdin.readline().split()))
    arr.append(inp)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] > 0 and arr[k][j] > 0:
                arr[i][j] = max(arr[i][j], arr[i][k]+arr[k][j])

for i in range(N):
    for j in range(N):
        if arr[i][j] > 0 :
            print(1, end=" ")
        else :
            print(0, end=" ")
    print()