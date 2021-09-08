# 현재 board 상황에서 지워지는 block Erase & Count
def erase(m, n, board):
    # 중복 제거 방지 위해 Set 자료형으로 지워질 수 있는 블록 담음
    can_erase = set()
    # brute forcing으로 접근
    for i in range(m-1): # block 2*2이므로 m-1
        for j in range(n-1):
            if board[i][j] == "-": # 만약 빈 block이라면 건너뛰기
                continue
            # 4개 블럭 동시 check
            if (board[i][j] == board[i][j+1] and board[i][j+1] == board[i+1][j] 
                and board[i+1][j] == board[i+1][j+1]):            
                # 지울 수 있다면 can_erase에 저장
                can_erase.add((i, j))
                can_erase.add((i, j+1))
                can_erase.add((i+1, j))
                can_erase.add((i+1, j+1))

    count = len(can_erase) # 지울 수 있는 개수
    # 탐색이 끝난 후 can_erase 지우기
    for t in can_erase:
        board[t[0]][t[1]] = "-"

    # board 압축
    for i in range(n):
        for j in range(m-1, -1, -1):
            if board[j][i] == "-":
                for k in range(j-1, -1, -1): 
                    if board[k][i] != "-": # 위에서 알파벳 만나면 Drop
                        board[j][i] = board[k][i] # 치환
                        board[k][i] = "-" 
                        break
                
    # 지우기 성공하면 True, Count, board 반환
    if count > 0:
        return True, count, board
    # 지우기 실패하면 False, 0, board 반환
    else :
        return False, count, board
    
def solution(m, n, board):
    answer = 0
    # board 삭제 편리함을 위해 2차원 board 재생성
    new_board = [["" for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_board[i][j] = board[i][j]
    
    available = True # 게임을 계속할지 결정
    while available:
        # 함수 리턴 값 저장
        available, count, new_board = erase(m, n, new_board)
        answer += count # 정답 count 증가
    return answer