def solution(play_time, adv_time, logs):
    answer = '00:00:00'
    h, m, s = map(int,play_time.split(":"))
    length = h*3600+m*60+s
    board = [0 for _ in range(length+1)]
    for l in logs:
        start, end = l.split("-")
        sh, sm, ss = map(int, start.split(":"))
        stime = sh*3600+sm*60+ss
        eh, em, es = map(int, end.split(":"))
        etime = eh*3600+em*60+es
        board[stime] += 1
        board[etime] -= 1
        
    for i in range(1, len(board)):
        board[i] = board[i] + board[i-1]
        
    ah, am, ass = map(int, adv_time.split(":"))
    alength = ah*3600+am*60+ass
    benefit = sum(board[:alength])
    maxb = benefit

    for i in range(1, len(board)-alength+1):
        benefit = benefit-board[i-1]+board[i+alength-1]
        if maxb < benefit:
            maxb = benefit
            h = i // 3600
            m = (i % 3600) // 60
            s = (i % 3600) % 60
            answer = '{0:02d}'.format(h)+':'+'{0:02d}'.format(m)+':'+'{0:02d}'.format(s)
    return answer