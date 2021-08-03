from collections import deque
import sys

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    check = [0]*10001
    ans = ""
    dq = deque([[A, ""]])
    while dq:
        num, order = dq.popleft()
        if num == B:
            ans = order
            break
    
        if check[num] == 1:
            continue
        check[num] = 1
        d1 = num // 1000
        d2 = num // 100 - d1 * 10
        d3 = num // 10 - d1 * 100 - d2 * 10
        d4 = num % 10
        
        d = (2*num) % 10000
        dq.append([d, order+"D"])
        s = (num+9999) % 10000
        dq.append([s, order+"S"])
        l = d2*1000+d3*100+d4*10+d1
        dq.append([l, order+"L"])
        r = d4*1000+d1*100+d2*10+d3
        dq.append([r, order+"R"])
    print(ans)