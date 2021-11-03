from itertools import combinations

N, M = map(int, input().split())
board = []

chicken = []
homes = []

for y in range(N):
    arr = list(map(int, input().split()))
    for x in range(N):
        if arr[x] == 1:
            homes.append([y, x])
        elif arr[x] == 2:
            chicken.append([y, x])

answer = float('inf')
for candidate in list(combinations(chicken, M)):
    distance = [float('inf') for _ in range(len(homes))]
    for chick in candidate:
        for idx, home in enumerate(homes):
            distance[idx] = min(distance[idx], abs(home[0] - chick[0]) + abs(home[1] - chick[1]))

    answer = min(answer, sum(distance))
print(answer)