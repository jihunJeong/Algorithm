import sys

def recursive(N, r, c, ans):
    half = 2**(N-1)
    if N == 0:
        return ans

    if r >= half and c >= half:
        ans += (half**2)*3
        return recursive(N-1, r-half, c-half, ans)
    elif r >= half and c < half:
        ans += (half**2)*2
        return recursive(N-1, r-half, c, ans)
    elif r < half and c >= half:
        ans += (half**2)
        return recursive(N-1, r, c-half, ans)
    elif r < half and c < half:
        return recursive(N-1, r, c, ans)

N, r, c = map(int, sys.stdin.readline().split())

ans = 0
print(recursive(N, r, c, ans))