def solution(N, stages):
    answer = []
    loose = [0] * (N+1)
    info = [0] * (N+2)
    for s in stages:
        info[s] += 1
    total = len(stages)
    for n in range(1, N+1):
        if total == 0:
            break
        loose[n] = info[n] / total
        total -= info[n]
    for i in range(1,N+1):
        mn, mi = -1,-1
        for j in range(1, N+1):
            if loose[j] > mn:
                mn = loose[j]
                mi = j
        loose[mi] = -2
        answer.append(mi)
    return answer