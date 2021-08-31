n = int(input())
m = int(input())

route = [[987654321 for _ in range(n+1)] for _ in range(n+1)]
for r in range(m):
    n1, n2, c = map(int, input().split())
    route[n1][n2] = min(route[n1][n2], c)

for i in range(1,n+1):
    route[i][i] = 0


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            route[i][j] = min(route[i][j], route[i][k]+route[k][j])
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if route[i][j] == 987654321:
            print(0, end=" ")
        else :
            print(route[i][j], end=" ")
    print()