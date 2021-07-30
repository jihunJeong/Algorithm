from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    N = int(input())
    arr = input()
    if N == 0:
        if 'D' in p:
            print("error")
        else :
            print("[]")
        continue

    arr = deque(list(map(int, arr[1:-1].split(','))))

    direct, flag = 0, 0
    for i in p:
        if N == 0:
            flag = 1
            break
        if i == 'R':
            direct = abs(direct-1)
        elif i == 'D':
            N -= 1
            if direct:
                arr.pop()
            else :
                arr.popleft()
    
    if flag:
        print("error")
    else :
        print("[", end="")
        if direct:
            print(','.join(str(arr[i]) for i in range(len(arr)-1, -1, -1)), end="")
        else :
            print(','.join(str(e) for e in arr), end="")
        print("]")