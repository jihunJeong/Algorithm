def solution(n, s, a, b, fares):
    answer = 1000000000
    graph = [[1000000000 for _ in range(n+1)] for _ in range(n+1)]
    for k in range(1,n+1):
        graph[k][k] = 0
        
    for f in fares:
        n1, n2, c = f
        graph[n1][n2] = c
        graph[n2][n1] = c
        
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    for k in range(1, n+1):
        answer = min(answer, graph[k][s] + graph[k][a] + graph[k][b])
    return answer