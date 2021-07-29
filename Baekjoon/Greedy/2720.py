T = int(input())

coin = [25, 10, 5, 1]
for i in range(T):
    C = int(input())
    ans = [0]*4
    for j in range(4):
        ans[j] = C // coin[j]
        C -= ans[j]*coin[j]
    
    print(' '.join(str(c) for c in ans))