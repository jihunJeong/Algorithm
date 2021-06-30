N = int(input())

p = [[0, 0] for _ in range(N)]
for i in range(N):
    p[i][0], p[i][1] = map(int, input().split())

p = sorted(p, key=lambda x : (x[1], x[0]))
for i in range(N):
    print(f"{p[i][0]} {p[i][1]}")