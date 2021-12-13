import sys
import copy 
sys.setrecursionlimit(10**4)

N = int(sys.stdin.readline())

def dfs(board, i):
    count = 0
    if i == N - 1:
        for iter in range(N):
            flag = True
            for j in range(i):
                if board[j] == iter or abs(board[j] - iter) == abs(j - i):
                    flag = False
                    break
            if flag:
                count += 1
        return count

    for iter in range(N):
        flag = True
        for j in range(i):
            if board[j] == iter or abs(board[j] - iter) == abs(j - i):
                flag = False
                break
        if flag:
            board.append(iter)
            count += dfs(board, i+1)
            board.pop()
    return count

board = []
print(dfs(board, 0))