from collections import defaultdict

cnt = 0
T = int(input())
for i in range(T):
    dic = defaultdict(int)
    string = input()
    
    flag = True
    current = string[0]
    for s in string:
        if current == s:
            dic[s] += 1
        else :
            if dic[s] != 0:
                flag = False
                break
            else :
                dic[s] = 1
                current = s
    
    if flag:
        cnt += 1
    
print(cnt)