T = int(input())
for i in range(T):
    n = int(input())
    d = dict()
    for j in range(n):
        name, ty = input().split()
        if ty in d.keys():
            d[ty].append(name)
        else :
            d[ty] = [name]
            
    ans = 1
    for k in d.keys():
        ans = ans * (len(d[k])+1)
    ans -= 1
    print(ans)