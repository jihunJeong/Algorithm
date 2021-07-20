grid = []
ans = {-1:0, 0:0, 1:0}

def check(y,x,size):
    if size == 1:
        ans[grid[y][x]] += 1
        return 

    flag, n = True, grid[y][x]
    for i in range(size):
        for j in range(size):
            if grid[y+i][x+j] != n:
                flag = False
                break
        if not flag:
            break
    
    if flag:
        ans[n] += 1
    else :
        for i in range(3):
            for j in range(3):
                ns = size//3
                check(y+ns*i, x+ns*j, ns)

N = int(input())
for i in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

check(0, 0, N)
for key in ans.keys():
    print(ans[key])