N, M = map(int, input().split())

ans, divide, cnt = 1, 1, 1
for i in range(N,N-M,-1):
    ans *= i
    divide *= cnt
    cnt += 1
print(ans // divide)