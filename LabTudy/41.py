N, M = map(int, input().split())

parent = [i for i in range(N+1)]
graph = []

def find(v1):
    if parent[v1] == v1:
        return v1
    return find(parent[v1])    


def union(v1, v2, parent):
    if find(v1) > find(v2):
        parent[v1] = find(v2)
    else :
        parent[v2] = find(v1)


for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 1:
            graph.append((i+1, j+1, 1))


while graph:
    n1, n2, edge = graph.pop()
    if find(n1) != find(n2):
        union(n1, n2, parent)

route = list(map(int, input().split()))
flag = 0
for i in range(1, len(route)):
    if find(route[0]) != find(route[i]):
        print("NO")
        flag = 1
        break
if not flag:
    print("Yes")
