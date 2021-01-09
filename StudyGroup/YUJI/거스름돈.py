from collections import deque
import copy

def solution(n, money):
    answer = 0
    money = sorted(money, reverse = True)
    dq = deque([[n, 0]])
    cnt_money = len(money)
    
    while dq:
        num, level = dq.popleft()
        for cnt in range((num // money[level]) + 1):
            next_num = num - (money[level]*cnt)
            if next_num == 0:
                answer += 1
            elif next_num >= money[-1] and level+1 < cnt_money:
                if level+1 == cnt_money:
                    if next_num % money[-1] == 0:
                        answer += 1
                    continue
                dq.append([next_num, level+1])
            
    return answer