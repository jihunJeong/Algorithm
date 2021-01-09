import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [[0 for x in range(n+1)] for y in range(n+1)]

    li = list(sys.stdin.readline().split())
    sorted_li = sorted(li)

    for y in range(1,n+1):
        for k in range(1, n+1):
            if li[y-1] == sorted_li[k-1]:
                arr[y][k] = arr[y-1][k-1]+1
                break
            else :
                arr[y][k] = max(arr[y-1][k], arr[y][k-1])
    
    print(max(max(arr)))