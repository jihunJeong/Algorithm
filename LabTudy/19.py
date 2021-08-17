arr = []

def recurrent(num, cnt, ans, info):
    if cnt == N:
        arr.append(ans)
    
    for i in range(4):
        if info[i] == 0:
            continue

        if i == 0:
            nans = ans + num[cnt]
        elif i == 1:
            nans = ans - num[cnt]
        elif i == 2:
            nans = ans * num[cnt]
        elif i == 3:
            if ans < 0:
                nans = (abs(ans) // num[cnt]) * -1
            else :
                nans = ans // num[cnt]
        
        info[i] -= 1
        recurrent(num, cnt+1, nans, info)
        info[i] += 1
        
N = int(input())
num = list(map(int, input().split()))
info = list(map(int, input().split()))
recurrent(num, 1, num[0], info)
print(max(arr))
print(min(arr))