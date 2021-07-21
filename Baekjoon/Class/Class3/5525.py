import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
string = sys.stdin.readline()

idx, ans = 0, 0
current = False
while idx < M:
    if current:
        if string[idx+1]+string[idx+2] == "OI":
            ans += 1
            idx += 2
        else :
            current = False
            idx += 1
    else :
        flag = True
        for i in range(2*N+1):
            if (i % 2 == 0 and string[idx+i] != 'I') or (i % 2 == 1 and string[idx+i] != 'O'):
                idx += i
                if string[idx] == 'O':
                    idx += 1
                flag = False
                break
        if flag:
            idx += 2*N
            ans += 1
            current = True
            
print(ans)