import heapq
from collections import defaultdict

def find(parent, a):
    if parent[a] == a:
        return a
    return find(parent, parent[a])

def union(parent, a, b):
    x = find(parent, a)
    y = find(parent, b)

    if x <= y:
        parent[y] = x
    else :
        parent[x] = y
    return parent

N = int(input())
x, y, z = [], [], []
for i in range(N):
    node = list(map(int, input().split()))
    x.append([node[0], i])
    y.append([node[1], i])
    z.append([node[2], i])

x, y, z = sorted(x), sorted(y), sorted(z)
hp = []
for i in range(N-1):
    heapq.heappush(hp, (x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    heapq.heappush(hp, (y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    heapq.heappush(hp, (z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

parent = [i for i in range(N)]
count, answer = 0, 0
while count < N and hp:
    dist, n1, n2 = heapq.heappop(hp)
    if find(parent, n1) == find(parent, n2):
        continue;
    
    count += 1
    answer += dist
    union(parent, n1, n2)
print(answer)