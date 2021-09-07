import heapq as hq

def solution(food_times, k):
    # 전체 시간보다 k가 크거나 같으면 -1
    if sum(food_times) <= k:
        return -1
    answer = 0
    hp = [] # heap
    for idx, time in enumerate(food_times):
        hq.heappush(hp, (time, idx+1))
    
    times = 0 # 이전에 섭취한 시간
    length = len(hp)
    
    while k - (hp[0][0]-times) * length >= 0:
        time, idx = hq.heappop(hp)
        time -= times
        k = k - time*length
        length -= 1
        times += time
    
    hp = sorted(hp, key=lambda x : x[1])
    answer = hp[k % length][1]
    
    return answer