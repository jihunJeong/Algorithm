from collections import deque

N, K = map(int, input().split())

check = [0 for _ in range(100001)]
s = deque([[N, 0]])

while s:
    [p, t] = s.popleft()
    if p == K:
        print(t)
        break
    
    if p < 0 or p > 100000 or check[p] == 1:
        continue
    check[p] = 1

    s.extend([[p-1,t+1],[p+1,t+1],[p*2,t+1]])