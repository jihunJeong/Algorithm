import copy

def solution(key, lock):
    answer = False
    N, M = len(lock), len(key)
    
    for i in range(4):
        for y in range(N+M-1):
            for x in range(N+M-1):
                board = [[0 for _ in range(N+2*M-2)] for _ in range(N+2*M-2)]
                chk_flag = True
                for key_y in range(M):
                    for key_x in range(M):
                        board[y+key_y][x+key_x] = key[key_y][key_x]

                for lock_y in range(N):
                    for lock_x in range(N):
                        board[M-1+lock_y][M-1+lock_x] += lock[lock_y][lock_x]
                        if board[M-1+lock_y][M-1+lock_x] != 1:
                            chk_flag = False
                            break
                    if not chk_flag:
                        break

                if chk_flag:
                    return True
        
        rotate_key = [[0 for _ in range(N)] for _ in range(N)]
        for y in range(M):
            for x in range(M):
                rotate_key[x][M-y-1] = key[y][x]
        key = copy.deepcopy(rotate_key)
        
    return answer