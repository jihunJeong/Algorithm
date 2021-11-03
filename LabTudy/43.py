import heapq

def find(parent, x):
    if parent[x] == x:
        return x
    
    return find(parent, parent[x])


def union(parent, a, b):
    x = find(parent, a)
    y = find(parent, b)

    if x < y:
        parent[y] = x
    else :
        parent[x] = y

N, M = map(int, input().split())
hp = []

parent = [i for i in range(N)]

answer = 0
for _ in range(M):
    n1, n2, cost = map(int, input().split())
    heapq.heappush(hp, (cost, (n1, n2)))
    answer += cost

count = 0
while count < N and hp:
    cost, (n1, n2) = heapq.heappop(hp)
    if find(parent, n1) == find(parent, n2):
        continue

    union(parent, n1, n2)
    count += 1
    answer -= cost
print(answer)

