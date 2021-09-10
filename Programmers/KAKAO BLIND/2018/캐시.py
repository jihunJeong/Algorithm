def solution(cacheSize, cities):
    answer = 0
    
    cache = dict() # cache에 도시가 있는지 판단
    timestamp = 0 # LRU를 위한 timestamp
    for city in cities:
        city = city.lower() # 대소문자 구분 안함
        timestamp += 1
        if cacheSize == 0: # 계속해서 Cache miss 처리
            answer += 5
        elif city in cache.keys(): # cache hit
            answer += 1
            cache[city] = timestamp
        else : # cache miss
            if len(cache.keys()) >= cacheSize: # cache에 이미 다 차있다면
                lru = 100001 # LRU Time 변수
                changed = "" # 교체할 city 변수
                for key in cache.keys():
                    if cache[key] < lru:
                        lru = cache[key]
                        changed = key
                del cache[changed] # 삭제    
            cache[city] = timestamp # 새로운 도시 추가
            answer += 5
    return answer