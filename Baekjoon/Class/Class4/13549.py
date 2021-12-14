import heapq

N, K = map(int, input().split())

visited = [0 for _ in range(100001)]
visited[N] = 1

hp = []
heapq.heappush(hp, (0, N))

while hp:
    step, v = heapq.heappop(hp)
    if v == K:
        print(step)
        break
    
    if v < K and 2*v <= 100000 and visited[2*v] == 0:
        heapq.heappush(hp, (step, 2*v))
        visited[2*v] = 1
    if v < K and v+1 <= 100000 and visited[v+1] == 0:
        heapq.heappush(hp, (step+1, v+1))
        visited[v+1] = 1
    if v >= 1 and visited[v-1] == 0:
        heapq.heappush(hp, (step+1, v-1))
        visited[v-1] = 1

