def solution(record):
    dic = dict()
    for r in record:
        inp = r.split()
        if inp[0] == "Enter":
            dic[inp[1]] = inp[2]
        elif inp[0] == "Change":
            dic[inp[1]] = inp[2]

    answer = []
    for r in record:
        inp = r.split()
        if inp[0] == "Enter":
            answer.append(dic[inp[1]]+"님이 들어왔습니다.")
        elif inp[0] == "Leave":
            answer.append(dic[inp[1]]+"님이 나갔습니다.")
    
    return answer