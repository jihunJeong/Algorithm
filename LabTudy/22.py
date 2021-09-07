from collections import deque

def get_next_pos(pos, board):
    rst = [] # pos에 해당하는 이동 가능한 위치 반환 결과
    # Unpacking
    p1, p2 = list(pos)
    p1y, p1x, p2y, p2x = p1[0], p1[1], p2[0], p2[1]
    
    # 상하좌우 이동
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    for i in range(4):
        np1y, np1x = p1y+dy[i], p1x+dx[i]
        np2y, np2x = p2y+dy[i], p2x+dx[i]
        
        # 경계 여부 Check
        if board[np1y][np1x] == 0 and board[np2y][np2x] == 0:
            rst.append({(np1y, np1x), (np2y, np2x)})
    
    # 회전 이동 시작
    # Y 위치 동일 
    if p1y == p2y: 
        for i in [-1, 1]: # 기준점에서 X는 동일하고 Y만 회전 됨
            # 회전되는 방향에 경계가 없어야 함
            if board[p1y + i][p1x] == 0 and board[p2y + i][p2x] == 0:
                rst.append({(p1y, p1x), (p1y + i, p1x)})
                rst.append({(p2y, p2x), (p2y + i, p2x)})
    # X 위치 동일
    if p1x == p2x:
        for i in [-1, 1]: # 기준점에서 Y는 동일하고 X만 회전 됨
            # 회전되는 방향에 경계가 없어야 함
            if board[p1y][p1x + i] == 0 and board[p2y][p2x + i] == 0:
                rst.append({(p1y, p1x), (p1y, p1x + i)})
                rst.append({(p2y, p2x), (p2y, p2x + i)})
    return rst

def solution(board):
    answer = 0
    
    N = len(board) # Board Size
    new_board = [[1 for _ in range(N+2)] for _ in range(N+2)] # 외곽에 경계있는 것으로 변환
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]
    
    # BFS 시작
    start = {(1, 1),(1, 2)}
    visited = [start] # position 방문 처리
    dq = deque() #Start pos부터 시작
    dq.append((start, 0))
    while dq:
        pos, cnt = dq.popleft()
        # 최종 목적지인 (N,N) 위치까지 도달했으면 종료
        if (N, N) in pos:
            answer = cnt
            break
            
        # 현재 pos에서 이동 가능한 위치
        for next_pos in get_next_pos(pos, new_board):
            # 가능한 위치가 방문하지 않았다면 queue에 삽입
            if next_pos not in visited:
                dq.append((next_pos, cnt+1))
                visited.append(next_pos) # 방문 Check -> 중복 방문 제거
            
    return answer