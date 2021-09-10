def solution(n, arr1, arr2):
    '''
    n은 정사각형 변의 길이, arr1, arr2가  숫자를 통해들어옴
    각 숫자는 2진수 변환 후 n자리로 변환 해서 답 도출
    '''
    answer = []
    board = [[0 for _ in range(n)] for _ in range(n)] # 지도
    for idx, num in enumerate(arr1):
        binary = "" # 이진수 담는 변수
        while num > 0: # 이진수 변환 시작
            remainder = num % 2
            num = num // 2
            binary = str(remainder) + binary
        i = n-1
        for bit in range(len(binary)-1, -1, -1): # 지도에 assign
            board[idx][i] = int(binary[bit])
            i -= 1
    
    for idx, num in enumerate(arr2):
        binary = "" # 이진수 담는 변수
        while num > 0: # 이진수 변환 시작
            remainder = num % 2
            num = num // 2
            binary = str(remainder) + binary
        i = n-1
        for bit in range(len(binary)-1, -1, -1): # 지도에 assign
            board[idx][i] = max(int(binary[bit]), board[idx][i]) # 둘 중에 하나라도 1이면 1 저장
            i -= 1
    
    for i in range(n):
        ans = ""
        for j in range(n):
            if board[i][j] == 1:
                ans = ans + "#"
            else :
                ans = ans + " "
        answer.append(ans)
    return answer