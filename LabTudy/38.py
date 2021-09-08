N, M = map(int, input().split())

info = [[float('inf') for _ in range(N+1)] for _ in range(N+1)] # 모든 점 쌍의 최단 경로를 담는 배열
for i in range(1, N+1):
    info[i][i] = 0 # 각 노드의 경로는 0

# Graph Edge Update
for _ in range(M):
    s, e = map(int, input().split()) # 시작점, 끝점
    info[s][e] = 1 # Edge insert

# 플로이드 워셜 알고리즘 진행
for k in range(1, N+1): # 지나는 점 k
    for i in range(1, N+1): # 시작 점 i
        for j in range(1, N+1): # 끝나는 점 j
            # 기존 존재 경로보다 K 지나는 경로가 최단일 때 Update
            info[i][j] = min(info[i][j], info[i][k] + info[k][j])

ans = 0 # 순위를 알 수 있는 점 개수 answer 값
# 모든 점에 대해 순위 파악
for i in range(1, N+1):
    fail = False # 순위 파악 안 될시 True
    for j in range(1, N+1): # i -> j 또는 j -> i의 경로가 있는지 파악
        # 두 경로다 Infinite이면 경로 존재 X 순위 알 수 없음
        if info[i][j] == float('inf') and info[j][i] == float('inf'):
            fail = True # 순위 알 수 없으면 종료
            break
    
    if not fail: # fail이 True가 아니라면
        ans += 1 # 순위 Count 1 증가
print(ans)