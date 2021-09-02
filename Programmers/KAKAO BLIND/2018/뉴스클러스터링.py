import re
from collections import defaultdict
def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    s1 = defaultdict(int)
    total = 0
    for i in range(0, len(str1)-1):
        if 97 <= ord(str1[i]) <= 122 and 97 <= ord(str1[i+1]) <= 122:
            temp = str1[i] + str1[i+1]
            s1[temp] += 1
            total += 1
    cnt = 0
    for i in range(0, len(str2)-1):
        if 97 <= ord(str2[i]) <= 122 and 97 <= ord(str2[i+1]) <= 122:
            temp = str2[i] + str2[i+1]
            if s1[temp] > 0:
                cnt += 1
                s1[temp] -= 1
            else :
                total += 1
    if total == 0:
        answer = 65536
    else :
        answer = (cnt / total) * 65536 // 1
    return answer