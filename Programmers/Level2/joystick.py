def solution(name):
    answer = 0

    idx = 0
    visited = [0 for x in range(len(name))]
    remain = len(name)
    while remain > 0:
        if visited[idx] != 1 and name[i] != 'A':
            visited[idx] = 1
            cnt = min(ord(name[i]) - ord('A'), ord('Z')-ord(name[i])+1)
            answer += cnt
        
        

    print(answer)
    return answer

if __name__ == "__main__":
    solution("JEROEN")
    solution("JAN")