def solution(lines):
    answer = 0
    table = []
    for l in lines:
        date, time, count = l.split()
        temp, ms = time.split(".")
        h, m, s = map(int, temp.split(":"))
        end = (h*3600+m*60+s)*1000+int(ms)
        start = end - float(count[:-1])*1000+1
        table.append([start, end])
    for i in range(len(table)):
        f, l = table[i]
        cnt = 0
        for j in range(len(table)):
            tf, tl = table[j]
            if not (tl < l or tf >= l + 1000):
                cnt += 1
        answer = max(answer, cnt)
    return answer