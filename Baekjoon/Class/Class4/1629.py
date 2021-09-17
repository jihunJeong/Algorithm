def divide_conquer(A, B, C):
    if B == 1:
        return A % C

    temp = divide_conquer(A, B//2, C)

    if B % 2 == 0:
        rst = (temp * temp) % C
    else :
        rst = (temp * temp * A) % C
    return rst

A, B, C = map(int, input().split())
ans = divide_conquer(A, B, C)
print(ans)