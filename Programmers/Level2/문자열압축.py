def solution(s):
    answer = len(s)
    for i in range(1,len(s)):
        sub_ans = ""
        start = 0
        pre_sub = s[0:i]
        count = 1
        for j in range(i, len(s), i):
            sub = s[j:j+i]
            if sub == pre_sub:
                count += 1
            else :
                if count == 1:
                    sub_ans += pre_sub
                else :
                    sub_ans += str(count) + pre_sub
                count = 1
                pre_sub = sub
        if count == 1:
            sub_ans += pre_sub
        else :
            sub_ans += str(count) + pre_sub
        answer = min(answer, len(sub_ans))
    return answer