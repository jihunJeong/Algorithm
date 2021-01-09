import math
import sys

sys.setrecursionlimit(10**6)

if __name__ == "__main__":
    a, b = map(int, input().split())
    if a % 2 == 0:
        print((a//2) * (b*2))
    elif a == 1:
        print(b*2)
    else :
        cnt = (a-3) // 2 * (b*2)
        cnt += 3*b
        print(cnt)