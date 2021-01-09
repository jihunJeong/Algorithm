import sys

if __name__ == "__main__":
    n, m = map(int,sys.stdin.readline().split())
    arr = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        li = list(map(int, sys.stdin.readline().split()))
        arr[i] = li

    for i in range(m):
        x, y, f = map(int, sys.stdin.readline().split())
        nx = x -1
        ny = y - 1
        max_cnt = 0
        
        cnt, sum_f = 0, 0
        y, x = ny, nx
        while True:
            sum_f += arr[y][x]
            if sum_f <= f:
                cnt += 1
            else :
                break
            y = y + 1  
            if y >= n:
                break 
        max_cnt = max(max_cnt, cnt)

        cnt, sum_f = 0, 0
        y, x = ny, nx
        while True:
            sum_f += arr[y][x]
            if sum_f <= f:
                cnt += 1
            else :
                break
            x = x + 1
            if x >= n:
                break 
        max_cnt = max(max_cnt, cnt)

        cnt, sum_f = 0, 0
        y, x = ny, nx
        while True:
            sum_f += arr[y][x]
            if sum_f <= f:
                cnt += 1
            else :
                break
            y = y - 1
            if y < 0:
                break 
        max_cnt = max(max_cnt, cnt)

        cnt, sum_f = 0, 0
        y, x = ny, nx
        while True:
            sum_f += arr[y][x]
            if sum_f <= f:
                cnt += 1
            else :
                break
            x = x - 1
            if x < 0:
                break 
        max_cnt = max(max_cnt, cnt)

    
        if max_cnt <= 0:
            print("Silver Pantheon")
        else : 
            print(max_cnt)