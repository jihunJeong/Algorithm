N = int(input())

people = [] 
for i in range(N):
    w, h = map(int, input().split())
    people.append([w, h])

ans = []
for i in range(N):
    s = 1
    for j in range(N):
        if i == j:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            s += 1
    ans.append(s)

for i in range(N):
    print(ans[i], end=" ")