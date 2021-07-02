K = int(input())

s = []
for i in range(K):
    n = int(input())

    if n == 0:
        s.pop()
    else :
        s.append(n)

print(sum(s))