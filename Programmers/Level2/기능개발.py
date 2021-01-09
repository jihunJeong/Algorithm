from collections import deque
import math

def solution(progresses, speeds):
    dq = deque()
    answer = []
    for i in range(len(progresses)):
        cnt = math.ceil((100-progresses[i]) // speeds[i])
        dq.append(cnt)
    while dq:
        max_day = dq[0]
        ans_cnt = 0
        while True:
            if dq[0] <= max_day:
                dq.popleft()
                ans_cnt += 1
            else :
                break
                
        answer.append(ans_cnt)
    
    return answer