from collections import deque

T = int(input())

for i in range(T):
    ans = 1
    cnt, pos = map(int, input().split())

    input_li = list(map(int, input().split()))
    dq = deque([[0, x] for x in input_li])
    dq[pos][0] = 1
    while dq:
        if dq[0][1] == max(dq, key=lambda x : x[1])[1]:
            info = dq.popleft()
            if info[0] == 1:
                print(ans)
                break
            ans += 1
        else :
            info = dq.popleft()
            dq.append(info)