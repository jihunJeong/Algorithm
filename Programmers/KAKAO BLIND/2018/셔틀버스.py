# n : 셔틀 횟수 t : 간격 m : 최대 승객 09:00 시작
# timetable은 최소 길이 1이고 최대 길이 2000 HH:MM
from collections import defaultdict

def solution(n, t, m, timetable):
    answer = ''
    bus = defaultdict(list)
    bustable = []
    bus_time  = 9 * 60
    for i in range(n):
        bustable.append(bus_time)
        bus_time += t
    timetable = sorted(timetable)
    for tt in timetable:
        th, tm = map(int, tt.split(":"))
        arrived = th*60+tm
        for i in range(n):
            if bustable[i] >= arrived and len(bus[bustable[i]]) < m:
                bus[bustable[i]].append(arrived)
                break
    finaltime = 9*60 + t * (n-1)
    finalh, finalm = finaltime // 60, finaltime % 60
    if len(bus[finaltime]) < m:
        answer = '{0:02d}'.format(finalh)+":"+'{0:02d}'.format(finalm)
    else :
        savetime = sorted(bus[finaltime])[-1]-1
        lasth, lastm = savetime // 60, savetime % 60
        answer = '{0:02d}'.format(lasth)+":"+'{0:02d}'.format(lastm)
    return answer