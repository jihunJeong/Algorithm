# 현재 x, y 좌표에서 안정 되어 있는지
def check(board):
    n = len(board)
    for i in range(n): # x 좌표
        for j in range(1, n): # y 좌표 바닥은 항상 ok
            for k in board[i][j]:
                if k == 0: # 기둥
                    # 기둥 아래에 기동이 있거나 또는 보의 한 쪽 끝 부분에 있지 않다면 안정하지 않음
                    if not (0 in board[i][j-1] or 1 in board[i-1][j]
                            or 1 in board[i][j]):
                        return False
                else : # 보
                    # 보의 한 쪽 끝 부분이 기둥 위에 있거나 또는 양쪽 부분이 다른 보와 동시에
                    # 연결되어 있지 않으면 안정하지 않음
                    if not ((0 in board[i][j-1] or 0 in board[i+1][j-1])
                            or (1 in board[i-1][j] and 1 in board[i+1][j])):
                        return False
    return True
                
# 조건을 build 하는 함수
def build(x, y, a, b, board):
    if b == 0: # 삭제
        board[x][y].remove(a)
        if not check(board): # 지우고 나서 조건 만족 안한다면
            board[x][y].append(a)
    else : # 추가
        board[x][y].append(a)
        if not check(board): # 설치하고 나서 조건 만족 안한다면
            board[x][y].remove(a)
    return board

def solution(n, build_frame):
    answer = []
    # n : 벽면의 크기
    board = [[[] for _ in range(n+1)] for _ in range(n+1)] # 구조물 정보 저장 배열
    
    for frame in build_frame:
        # [x, y, a, b]
        x, y, a, b = frame # build 정보 a : type, b : option
        board = build(x, y, a, b, board) # 설치 혹은 철거가 가능하다면 시행
    
    # 결과물 도출
    for i in range(n+1): # x 좌표
        for j in range(n+1): # y 좌표
            for t in sorted(board[i][j]): # 좌표가 같은 경우 기둥이 보보다 먼저
                answer.append([i, j, t])
    
    return answer